Skip to content
Why GitHub? 
  Team
Enterprise
Explore 
Marketplace
Pricing 
Search

Sign in
Sign up
d2525456d
/
  okbrau
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
okbrau/CTDLGT_R/BT06_DanhSachLienKetDon.R
@d2525456d
d2525456d BT06
Latest commit 761fa53 3 days ago
History
1 contributor
85 lines (77 sloc)  1.67 KB

create_emptyenv <- function() {
  emptyenv()
}

isEmpty <- function(llist) {
  if(class(llist)!= "linkList") warning("Not linkList class")
  identical(llist, create_emptyenv())
}

linkListNode <- function(val, node=NULL) {
  llist <- new.env(parent=create_emptyenv())
  llist$element <- val
  llist$nextnode <- node
  class(llist) <- "linkList"
  llist
}

LList <-linkListNode(5,linkListNode(2,create_emptyenv()))

setNextNode<-function(llist){
  llist$nextnode
}
setNextElement<-function(llist){
  llist$element
}

sizeLinkList<-function(llist, size=0){
  if (isEmpty(llist)) 
  {
    return(size)
  } else
  {
    size<-size+1L
    sizeLinkList(llist$nextnode, size)
  }
}

addElement<-function(new, llist) 
{
  if (isEmpty(llist)) {
    llist<-linkedlist(new)
  } else
  {
    llist<-linkListNode(llist, new)
  }
  llist
}

delElement<-function(llist, pos=NULL){
  if(is.null(pos)) warning("Nothing to delete")
  listsize<-sizeLinkList(llist)
  if(pos>listsize) stop("Position greater than size of list")
  if (isEmpty(llist)) {
    warning("Empty List")
  } else if(pos==1){
    PreviousNode<-llist$nextnode
  } else 
  {
    PreviousNode<-linkListNode(llist$element)
    for(i in 1:(listsize-1)){
      if(pos==(i+1)){
        PreviousNode$nextnode<-setNextNode(llist$nextnode)
      } else
      {
        PreviousNode$nextnode<-llist$nextnode
        llist<-llist$nextnode
      }
    }
  }
  return(PreviousNode)
}

findItem<-function(llist, item, pos=0, itemFound=FALSE){
  if (itemFound==TRUE) 
  {
    return(itemFound)
  } else if(isEmpty(llist)){
    return(FALSE)
  } else
  {
    pos<-pos+1L
    if(llist$element==item) itemFound<-TRUE
    findItem(llist$nextnode, item, size, itemFound)
  }
}
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete