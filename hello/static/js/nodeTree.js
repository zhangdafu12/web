// JavaScript Document
var zNodes;//��Ŀ��json��ʽ�ַ���
var setting = {
	view: {
		dblClickExpand: false,//˫���ڵ�����չ�������𣩽ڵ�
		showLine: true,//��ʾ������
		selectedMulti: false//�Ƿ�֧�ֶ�ѡ����ctrl����
	},
	data: {
		simpleData: {
			enable:true,
			idKey: "nodeID",//json���нڵ�ID��KEY
			pIdKey: "parentID",//json���и��ڵ�ID��KEY
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
			//����xml�����е�node�ڵ㣬��ȡ�����Լ��ӽڵ�Ϊjson��ʽ�ַ���
			$(data).find('node').each(function(){
				zNodes += 
					"{" + 
						"\"name\":\"" + $(this).find("nodeName").text() + "\"," + //��ȡ�ӽڵ�����
						"\"nodeID\":\"" + $(this).attr("nodeID") + "\"," + //��ȡ�ڵ�������Ϣ
						"\"parentID\":\"" + $(this).attr("parentID") + "\"," + 
						"\"nodeUrl\":\"" + $(this).attr("nodeUrl") + "\"," + 
						"\"articleNum\":\"" + $(this).attr("articleNum") + "\"" +
					"},";
			});
			zNodes = zNodes.substring(0,zNodes.length-1);
			zNodes += "]";
			$.fn.zTree.init($("#tree"), setting, jQuery.parseJSON(zNodes));//������Ŀ����jQuery.parseJSON(zNodes)��json��ʽ�ַ���ת��Ϊjson����
			$("#nodeIframe").attr("src","http://www.2345.com/?kang0533");
		},"xml"
	);
});