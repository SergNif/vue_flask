function xpath(el) {
  if (typeof el == "string") return document.evaluate(el, document, null, 0, null)
  if (!el || el.nodeType != 1) return ''
  if (el.id) return "//*[@id='" + el.id + "']"
  var sames = [].filter.call(el.parentNode.children, function (x) { return x.tagName == el.tagName })
  return xpath(el.parentNode) + '/' + el.tagName.toLowerCase() + (sames.length > 1 ? '['+([].indexOf.call(sames, el)+1)+']' : '')
}

$(document).ready(function($){
	$('body').on("click",function(event){
		alert(xpath(event));
	});
});