import crypto from 'crypto'

var baseURL = "http://localhost:8080"
var backURL = "http://172.16.20.3:8000"

function prettify (str) {
  let s = ""
  s += str[0].toUpperCase()
  for (let i = 1; i < str.length; i++) {
    if (str[i] == "_")
      s += " "
    else if (str[i - 1] == "_" || str[i - 1] == "-" || str[i - 1] == " ")
      s += str[i].toUpperCase()
    else
      s += str[i]
  }
  return s;
}

function randomValue (len) {
  return crypto.randomBytes(Math.ceil(len/2))
    .toString('hex')               // convert to hexadecimal format
    .slice(0,len).toUpperCase();   // return required number of characters
}

function getUniqueId (prefix, length) {
  let id = prefix + randomValue(length)
  while (document.getElementById(id))
    id = prefix + randomValue(length)
  return id
}

function genBackendURL (str) {
  return backURL + "/" + str + "?format=json"
}


export {
  backURL,
  baseURL,
  prettify,
  randomValue,
  getUniqueId,
  genBackendURL
}
