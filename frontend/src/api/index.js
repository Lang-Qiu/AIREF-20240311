//配置全局访问接口地址
let commonUrl = 'http://localhost:8088'
let baseUrl = {
    loginUrl: commonUrl + '/auth/login/',
    registerUrl: commonUrl + '/auth/register/',
    uploadUrl: commonUrl + '/upload/',
    uploadTextUrl: commonUrl + '/uploadText/'
}

export default baseUrl