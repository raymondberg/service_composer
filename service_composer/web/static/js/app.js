function recurseOpen(object){
  if(object == document) { return }
  if(object.tagName == "DETAILS") { object.open = true }

  recurseOpen(object.parentNode);
}

function expand(component) {
  collapseAll();

  $("."+component).each(function(_, object) {
    recurseOpen(object)
  });
}

function collapseAll() {
  $("details").each(function(_, object) { object.open = false });
}
