tower <- function(n, toa1,toa2,toa3){
  if (n == 1) {
    cat('chuyen tu',toa1,'sang',toa3, '\n')
  } else {
    tower(n-1,toa1,toa3,toa2)
    cat('chuyen tu',toa1,'sang',toa3, '\n')
    tower(n-1,toa2,toa1,toa3)}
}
tower(3,'tòa1','tòa2','tòa3')
