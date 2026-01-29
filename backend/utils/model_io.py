import torch
import onnx
import pickle
from onnx2torch import convert

class model_io:
    @staticmethod
    def export_torch_model_to_onnx(
        net, dummy_input, path_and_filename, input_names=None, output_names=None
    ):
        torch.onnx.export(net, dummy_input, path_and_filename, input_names, output_names)

    @staticmethod
    def load_and_check_onnx_model(path_and_filename):
        net = onnx.load(path_and_filename)
        try:
            onnx.checker.check_model(net)

            # 获得输入大小
            input_shape = net.graph.input[0].type.tensor_type.shape.dim
            print("Input shape:", tuple(d.dim_value for d in input_shape))

            # 获取输出大小
            output_shape = net.graph.output[0].type.tensor_type.shape.dim
            num_classes = output_shape[1].dim_value
            print("Number of classes:", num_classes)
        except onnx.checker.ValidationError as e:
            print("model is invalid: %s" % e)
        else:
            return convert(path_and_filename), input_shape, num_classes
    
    @staticmethod
    def load_model_by_struct(ModelClass, path_and_filename):
        model = ModelClass()
        ckpt = torch.load(path_and_filename)
        model.load_state_dict(ckpt["model_state_dict"])
        model.eval()
        return model

    @staticmethod
    def export_to_torchscript(model, path_and_filename):
        model_scripted = torch.jit.script(model)
        model_scripted.save(path_and_filename)

    @staticmethod
    def export_to_pickle(model, path_and_filename):
        with open(path_and_filename, 'wb') as f:
            pickle.dump(model, f)

    @staticmethod
    def load_model_by_torchscript(path_and_filename, device='cpu'):
        model = torch.jit.load(path_and_filename, map_location=device)
        model.eval()
        return model

    @staticmethod
    def load_model_by_pickle(path_and_filename, device='cpu'):
        with open(path_and_filename, 'rb') as f:
            model = pickle.load(f)
        model.to(device)
        model.eval()
        return model

