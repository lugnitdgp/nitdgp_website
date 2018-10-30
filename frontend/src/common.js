import crypto from 'crypto'

var baseURL = "http://localhost:8080"
var backURL = "https://admin.nitdgp.ac.in"

function stripDesc (str) {
  if (str.length < 54)
    return str.slice(3, -4)
  else
    return str.slice(3, 50) + "... More"
}

function stripDesc2 (str) {
  if (str.length < 104)
    return str.slice(3, -4)
  else
    return str.slice(3, 100) + "... More"
}

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

function genBackendURL (str, fromBackend=false) {
  if (fromBackend) {
    if (str[0] == "/")
      return backURL + str
    return str
  }
  if (str[0] != "/")
    str = "/" + str
  if (str[str.length - 1] != "/")
    str = str + "/"
  return backURL + str + "?format=json"
}


function range(start, stop, step) {
  if (typeof stop == 'undefined') {
    // one param defined
    stop = start;
    start = 0;
  }

  if (typeof step == 'undefined') {
    step = 1;
  }

  if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
    return [];
  }

  var result = [];
  for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
    result.push(i);
  }

  return result;
}


function convertNewsfeed(raw_data){

  const months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY",
                 "AUG", "SEPT", "OCT", "NOV", "DEC"]
  let notices = []
  let news_slide = []
  raw_data.map((news,index) => {
    let date = new Date(news.date)
    news.month = months[date.getMonth()]
    news.date = date.getDate()
    news.year = date.getFullYear()
    if (news.file != null || news.link || news.url) {
      if (news.file)
        news.link = news.file
      if (news.url)
        news.link = news.url
      news.link = genBackendURL(news.link, true)
    }
    news_slide.push(news)
    if ((index+1) % 4 == 0) {
      notices.push(news_slide)
       news_slide = []
    }
  })
  if (news_slide.length) {
    notices.push(news_slide)
  }
  return notices
}

export {
  backURL,
  baseURL,
  prettify,
  randomValue,
  getUniqueId,
  genBackendURL,
  range,
  convertNewsfeed,
  stripDesc,
  stripDesc2
}
