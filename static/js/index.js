$(document).ready(function(){
	var locationPath = location.pathname;
	var start = 1;
        var end = locationPath.indexOf("/", start);
        var menuTxt = locationPath.substring(start, end);
	$("#navmenu > li > a").each(function() {
                var pathName = this.pathname;
                var e = pathName.indexOf("/", start);
                var pn = pathName.substring(start, e);
		if(menuTxt == pn) {
			$(this).addClass("on");
                }
	});
	$.featureList(
		$(".slides_nav li"),
		$(".slides_box div"), 
		{
			start_item	:	0
		}
	);

	var btnCls = $(".listprod .prod_cls li")
	btnCls.hover(function(){
		btnCls.removeClass("hover");
		var index = $(this).addClass("hover").index();
		$(".listprod .prods .prod_list").attr("class", "prod_list")[index].className = "prod_list seleted";
	});
});
