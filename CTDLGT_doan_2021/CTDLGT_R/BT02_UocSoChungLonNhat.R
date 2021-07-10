UCLN <- function(a, b){
  if(b == 0){
    return(a)
  } else {
    return(UCLN(b, a%%b))
  }
}
UCLN(20,150)
