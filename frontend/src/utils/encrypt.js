import JSEncrypt from 'jsencrypt/bin/jsencrypt'

// 密钥对生成 http://web.chacuo.net/netrsakeypair
// '-----BEGIN RSA PUBLIC KEY-----'+
const publicKey = `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3tTOBXCbqnPrCE7vsR0T
UMOgoOTpsBpiwsfZVLzFPu/VmBB5DmEfMcusZqtgkflDju2VYy6Yy6oxiKz4nP7u
NLGATww9VeNRzQEN/YnT5wJT95gpkWAjvOVSde9pw1OceLaT/zhmiVUFrJr3l8P0
N/Jh8MjnIcpebR1O3T4blqYufy9gCG5QvRD6JKHRd4rqxOdQvlNdl2CPmNJBoVyG
02wuTJi8A0YFrITgUdWS0g/Dyd6MQWhIRDEG44NrU/Z2TkFHP87RoQ1Keu8jwQeJ
eI5ggpG4/IyzDPdhyeoavCzHzLNI5lcplgCwH8VfnZtopvaU/J9Ew9Ti7wBmRD9F
iwIDAQAB`
// '-----END RSA PUBLIC KEY-----'


// 加密
export function encrypt(txt) {
  const encryptor = new JSEncrypt()
  encryptor.setPublicKey(publicKey) // 设置公钥
  return encryptor.encrypt(txt) // 对需要加密的数据进行加密
}

// // 解密
// export function decrypt(txt) {
//   const encryptor = new JSEncrypt()
//   encryptor.setPrivateKey(privateKey)
//   return encryptor.decrypt(txt)
// }

