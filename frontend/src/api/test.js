import request from "@/utils/request";

export const getTestResultOne = ({ data_url, data_token, data_type }) => {
    const username = sessionStorage.getItem("username");
    return request.post('/api/data/', {
        username,
        data_url,
        data_token,
        data_type
    })
}

export const getTestResultTwo = ({ data_url, data_token, model_url, model_token }) => {
    const username = sessionStorage.getItem("username");
    return request.post('/api/model/', {
        username,
        data_url,
        data_token,
        model_url,
        model_token
    })
}

export const getTestResultThree = ({ data_url, data_token, model_url, model_token, attack_list }) => {
    const username = sessionStorage.getItem("username");
    return request.post('/api/attack/', {
        username,
        data_url,
        data_token,
        model_url,
        model_token,
        attack_list
    })
}
