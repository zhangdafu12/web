


var setting = {
    check: {
        enable: true//checkbox
    },
    view: {
        // addHoverDom: addHoverDom,
        //removeHoverDom: removeHoverDom,
        //addDiyDom: addDiyDom,
        selectedMulti: false,
        nameIsHTML: true //允许name支持html

    },
    edit: {
        // enable: true,
        // editNameSelectAll: false,
        //是否全部添加删除按钮
        // showRemoveBtn:true,
        // showRenameBtn:true//根节点是否删除
    },
    data: {
        simpleData: {
            enable: true
        }
    },
    callback: {
        beforeDrag: beforeDrag,//用户禁止拖动节点
        //sbeforeEditName: beforeEditName,//点击编辑时触发，用来判断该节点是否能编辑
        //beforeRemove: beforeRemove,//点击删除时触发，用来提示用户是否确定删除（可以根据返回值 true|false 确定是否可以删除）
        // beforeRename: beforeRename,//编辑结束时触发，用来验证输入的数据是否符合要求(也是根据返回值 true|false 确定是否可以编辑完
        //onRemove: onRemove,//(beforeRemove返回true之后可以进行onRemove)删除节点后触发，用户后台操作
        onRename: onRename,//编辑后触发，用于操作后台
    }
};
// var setting3 = {
//     check: {
//         enable: true//checkbox
//     },
//     view: {
//         addHoverDom: addHoverDom,
//         removeHoverDom: removeHoverDom,
//         addDiyDom: addDiyDom,
//         selectedMulti: false,
//         nameIsHTML: true //允许name支持html

//     },
//     edit: {
//         enable: true,
//         editNameSelectAll: false,
//         //是否全部添加删除按钮
//         showRemoveBtn:true,
//         showRenameBtn:true//根节点是否删除
//     },
//     data: {
//         simpleData: {
//             enable: true
//         }
//     },
//     callback: {
//         beforeDrag: beforeDrag,//用户禁止拖动节点
//         sbeforeEditName: beforeEditName,//点击编辑时触发，用来判断该节点是否能编辑
//         beforeRemove: beforeRemove,//点击删除时触发，用来提示用户是否确定删除（可以根据返回值 true|false 确定是否可以删除）
//         beforeRename: beforeRename,//编辑结束时触发，用来验证输入的数据是否符合要求(也是根据返回值 true|false 确定是否可以编辑完
//         onRemove: onRemove,//(beforeRemove返回true之后可以进行onRemove)删除节点后触发，用户后台操作
//         onRename: onRename,//编辑后触发，用于操作后台
//     }
// };




var zNodes2 =[
    { id:1, pId:0, name:"人员", open:true},
    { id:11, pId:1, name:"张11"},
    { id:12, pId:1, name:"张22"},
    { id:13, pId:1, name:"张33"},
    { id:2, pId:0, name:"职务", open:true},
    { id:21, pId:2, name:"财务1"},
    { id:22, pId:2, name:"财务12"},
    { id:23, pId:2, name:"财务13"},
    { id:3, pId:0, name:"科室", open:true},
    { id:31, pId:3, name:"开发1"},
    { id:32, pId:3, name:"开发12"},
    { id:33, pId:3, name:"开发13"}
];
var zNodes=[
    { id:1, pId:0, name:"数据", open:true},
    { id:11, pId:1, name:"文件1"},
    { id:12, pId:1, name:"文件12"},
    { id:13, pId:1, name:"文件13"},
    { id:2, pId:0, name:"API", open:true},
    { id:21, pId:2, name:"js1"},
    { id:22, pId:2, name:"js12"},
    { id:23, pId:2, name:"js13"},
    { id:3, pId:0, name:"网站", open:true},
    { id:31, pId:3, name:"taobao1"},
    { id:32, pId:3, name:"taobao12"},
    { id:33, pId:3, name:"taobao13"},
    { id:4, pId:0, name:"车辆", open:true},
    { id:41, pId:4, name:"tsl1"},
    { id:42, pId:4, name:"tsl12"},
    { id:43, pId:4, name:"tsl13"},
    { id:5, pId:0, name:"房屋", open:true},
    { id:51, pId:5, name:"内环1"},
    { id:52, pId:5, name:"内环12"},
    { id:53, pId:5, name:"内环13"},
];

// var zNodes3=[
//     { id:6, pId:0, name:"人员", open:true},
//     { id:61, pId:6, name:"张11"},
//     { id:62, pId:6, name:"张22"},
//     { id:63, pId:6, name:"张33"},
//     { id:7, pId:0, name:"职务", open:true},
//     { id:71, pId:7, name:"财务1"},
//     { id:72, pId:7, name:"财务12"},
//     { id:73, pId:7, name:"财务13"},
//     { id:8, pId:0, name:"科室", open:true},
//     { id:81, pId:8, name:"开发1"},
//     { id:82, pId:8, name:"开发12"},
//     { id:83, pId:8, name:"开发13"}
// ];




var log, className = "dark";
//添加下拉框
var IDMark_A = "_a";

function addDiyDom(treeId, treeNode) {
    if (treeNode.editNameFlag || $("#addBtn_"+treeNode.tId).length>0) return;
    var sObj = $("#" + treeNode.tId + IDMark_A);
    var addStr = "<select class='selDemo' id='diyBtn_" +treeNode.id+ "'><option value=1>1</option><option value=2>2</option><option value=3>3</option></select>";
    sObj.after(addStr);
    var btn = $("#addBtn_"+treeNode.id);
    if (btn) btn.bind("change", function(){alert("diy Select value="+btn.attr("value")+" for " + treeNode.name);});

}
//鼠标移入显示按钮
var newCount = 1;
function addHoverDom(treeId, treeNode) {
    var sObj = $("#" + treeNode.tId + "_span");
    if (treeNode.editNameFlag || $("#addBtn_"+treeNode.tId).length>0) return;

    var addStr = "<span class='button add' id='addBtn_" + treeNode.tId
        + "' title='add node' onfocus='this.blur();'></span>";
    sObj.after(addStr);
    var btn = $("#addBtn_"+treeNode.tId);
    if (btn) btn.bind("click", function(){
        var zTree = $.fn.zTree.getZTreeObj("treeDemo");
        zTree.addNodes(treeNode, {id:(100 + newCount), pId:treeNode.id, name:"new node" + (newCount++)});
        //return false;
    });
};
function beforeDrag(treeId, treeNodes) {
    return false;
}
function beforeEditName(treeId, treeNode) {
    className = (className === "dark" ? "":"dark");
    showLog("[ "+getTime()+" beforeEditName ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name);
    var zTree = $.fn.zTree.getZTreeObj("treeDemo");
    zTree.selectNode(treeNode);
    setTimeout(function() {
        if (confirm("进入节点 -- " + treeNode.name + " 的编辑状态吗？")) {
            setTimeout(function() {
                zTree.editName(treeNode);
            }, 0);
        }
    }, 0);
    return true;
}
function beforeRemove(treeId, treeNode) {
    className = (className === "dark" ? "":"dark");
    showLog("[ "+getTime()+" beforeRemove ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name);
    var zTree = $.fn.zTree.getZTreeObj("treeDemo");
    zTree.selectNode(treeNode);
    return confirm("确认删除 节点 -- " + treeNode.name + " 吗？");
}
function onRemove(e, treeId, treeNode) {
    showLog("[ "+getTime()+" onRemove ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name);
}
function beforeRename(treeId, treeNode, newName, isCancel) {
    className = (className === "dark" ? "":"dark");
    showLog((isCancel ? "<span style='color:red'>":"") + "[ "+getTime()+" beforeRename ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name + (isCancel ? "</span>":""));
    if (newName.length == 0) {
        setTimeout(function() {
            var zTree = $.fn.zTree.getZTreeObj("treeDemo");
            zTree.cancelEditName();
            alert("节点名称不能为空.");
        }, 0);
        return false;
    }
    return true;
}
function onRename(e, treeId, treeNode, isCancel) {
    showLog((isCancel ? "<span style='color:red'>":"") + "[ "+getTime()+" onRename ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name + (isCancel ? "</span>":""));
}
function showRemoveBtn(treeId, treeNode) {
    return !treeNode.isFirstNode;
}
function showRenameBtn(treeId, treeNode) {
    return !treeNode.isLastNode;
}
function showLog(str) {
    if (!log)
    log = $("#log");
    log.append("<li class='"+className+"'>"+str+"</li>");
    if(log.children("li").length > 8) {
        log.get(0).removeChild(log.children("li")[0]);
    }
}
function getTime() {
    var now= new Date(),
        h=now.getHours(),
        m=now.getMinutes(),
        s=now.getSeconds(),
        ms=now.getMilliseconds();
    return (h+":"+m+":"+s+ " " +ms);
}


function removeHoverDom(treeId, treeNode) {
    $("#addBtn_"+treeNode.tId).unbind().remove();
};
function selectAll() {
    var zTree = $.fn.zTree.getZTreeObj("treeDemo");
    zTree.setting.edit.editNameSelectAll =  $("#selectAll").attr("checked");
}

function selectAll2() {
    var zTree = $.fn.zTree.getZTreeObj("treeDemo2");
    zTree.setting.edit.editNameSelectAll=  $("#selectAll2").attr("checked");
}
function selectAll3() {
    var zTree = $.fn.zTree.getZTreeObj("treeDemo3");
    zTree.setting.edit.editNameSelectAll=  $("#selectAll3").attr("checked");
}





$(document).ready(function(){
    //从服务器读取数据并初始化树形图
    //loadDataFromServer(urlStr);
    //本例直接从模拟数据dataset.js读取
    var treedata=$.fn.zTree.init($("#treeDemo"), setting, zNodes);//获取数据
    treedata.expandAll(true);
    $("#selectAll").bind("click", selectAll);
    fuzzySearch('treeDemo','#key',null,true);  //初始化模糊搜索方法
//

    var treedata2=$.fn.zTree.init($("#treeDemo2"), setting, zNodes2);//获取数据
    treedata2.expandAll(true);
    $("#selectAll2").bind("click", selectAll2);
    fuzzySearch('treeDemo2','#key2',null,true);  //初始化模糊搜索方法   

    // var treedata3=$.fn.zTree.init($("#treeDemo3"), setting3, zNodes3);//获取数据
    // treedata3.expandAll(true);
    // $("#selectAll3").bind("click", selectAll3);
    // fuzzySearch('treeDemo3','#key3',null,true);  //初始化模糊搜索方法

});




/*
* 通过ajax方法从服务器获取数据并初始化树形图

function loadDataFromServer(urlStr){
    $.ajax({
        type: "get",
        dataType: "json",
        url: urlStr,  //服务请求地址
        success: function(data) {
            initThisZtree(data);//传入数据,初始化ztree
            fuzzySearch('book','#keyword',null,true); //初始化模糊搜索方法
        }
    });
}*/
//-->

