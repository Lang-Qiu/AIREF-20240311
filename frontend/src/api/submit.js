import request from "@/utils/request";

export const getSubmitResultOne = (url, token) => {
    return request.get('', {
        params: {
            data_url: url,
            data_token: token
        }
    })
}

export const getSubmitResultTwo = (data_url, data_token, model_url, model_token) => {
    return request.get('', {
        params: {
            data_url,
            data_token,
            model_url,
            model_token
        }
    })
}

export const getSubmitResultThree = (data_url, data_token, model_url, model_token, attack_list) => {
    return request.get('m1/3648993-0-default/title/submit', {
        params: {
            data_url,
            data_token,
            model_url,
            model_token,
            attack_list
        }
    })
}