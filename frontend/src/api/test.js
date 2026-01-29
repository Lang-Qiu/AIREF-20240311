import request from "@/utils/request";

export const getTestResultOne = ({ data_url, data_token, data_type }) => {
    return request.get('m1/3648993-0-default/test/data', {
        params: {
            data_url,
            data_token,
            data_type
        }
    })
}

export const getTestResultTwo = ({ data_url, data_token, model_url, model_token }) => {
    return request.get('m1/3648993-0-default/test/model', {
        params: {
            data_url,
            data_token,
            model_url,
            model_token
        }
    })
}

export const getTestResultThree = ({ data_url, data_token, model_url, model_token, attack_list }) => {
    return request.get('m1/3648993-0-default/test/attack', {
        params: {
            data_url,
            data_token,
            model_url,
            model_token,
            attack_list
        }
    })
}