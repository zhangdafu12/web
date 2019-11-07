// JavaScript Document
var zNodes;//栏目树json格式字符串
var setting = {
	view: {
		dblClickExpand: false,//双击节点名称展开（收起）节点
		showLine: true,//显示连接线
		selectedMulti: false//是否支持多选（按ctrl键）
	},
	data: {
		simpleData: {
			enable:true,
			idKey: "nodeID",//json串中节点ID的KEY
			pIdKey: "parentID",//json串中父节点ID的KEY
		}
	},
	callback: {
		onClick: function(event, treeId,treeNode) {
			$("#nodeIframe").attr("src",treeNode.nodeUrl);
		}
	}
};
$(document).ready(function(){
	$.post(
		"../../123.xml",
		function(data){
			zNodes="[";
			//遍历xml中所有的node节点，读取其属性及子节点为json格式字符串
			$(data).find('node').each(function(){
				zNodes += 
					"{" + 
						"\"name\":\"" + $(this).find("nodeName").text() + "\"," + //获取子节点数据
						"\"nodeID\":\"" + $(this).attr("nodeID") + "\"," + //获取节点属性信息
						"\"parentID\":\"" + $(this).attr("parentID") + "\"," + 
						"\"nodeUrl\":\"" + $(this).attr("nodeUrl") + "\"," + 
						"\"articleNum\":\"" + $(this).attr("articleNum") + "\"" +
					"},";
			});
			zNodes = zNodes.substring(0,zNodes.length-1);
			zNodes += "]";
			$.fn.zTree.init($("#tree"), setting, jQuery.parseJSON(zNodes));//加载栏目树，jQuery.parseJSON(zNodes)将json格式字符串转换为json对象
			$("#nodeIframe").attr("src","http://www.2345.com/?kang0533");
		},"xml"
	);
});