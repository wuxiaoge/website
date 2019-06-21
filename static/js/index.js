$(document).ready(function(){
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