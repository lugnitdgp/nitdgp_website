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


export {
  prettify
}
