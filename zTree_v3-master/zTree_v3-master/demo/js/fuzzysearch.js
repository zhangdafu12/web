/*
 * email: bigablecat@hotmail.com
 * Date: 2018-04-14
 */

/**
 * @param zTreeId the ztree id used to get the ztree object
 * @param searchField selector of your input for fuzzy search
 * @param isHighLight whether highlight the match words, default true
 * @param isExpand whether to expand the node, default false
 * 
 * @returns
 */	
 function fuzzySearch(zTreeId, searchField, isHighLight, isExpand){
	var zTreeObj = $.fn.zTree.getZTreeObj(zTreeId);//get the ztree object by ztree id
	if(!zTreeObj){
		alert("获取树对象失败");
	}
	var nameKey = zTreeObj.setting.data.key.name; //获取name属性的key
	isHighLight = isHighLight===false?false:true;//d除直接输入false的情况外,都默认为高亮
	isExpand = isExpand?true:false; // not to expand in default
	zTreeObj.setting.view.nameIsHTML = isHighLight; //allow use html in node name for highlight use
	
	var metaChar = '[\\[\\]\\\\\^\\$\\.\\|\\?\\*\\+\\(\\)]'; //js meta characters
	var rexMeta = new RegExp(metaChar, 'gi');//regular expression to match meta characters

	//过滤ztree显示数据
	function ztreeFilter(zTreeObj,_keywords,callBackFunc) {
		if(!_keywords){
			_keywords =''; //如果为空，赋值空字符串
		}

		// 查找符合条件的叶子节点
		function filterFunc(node) {
			if(node && node.oldname && node.oldname.length>0){
				node[nameKey] = node.oldname; //如果存在原始名称则恢复原始名称
			}
			//node.highlight = false; //取消高亮
			zTreeObj.updateNode(node); //更新节点让之前对节点所做的修改生效
			if (_keywords.length == 0) {
				//如果关键字为空,返回true,表示每个节点都显示
				zTreeObj.showNode(node);
				zTreeObj.expandNode(node,isExpand);//关键字为空时是否展开节点
				return true;
			}
			//节点名称和关键字都用toLowerCase()做小写处理
			if (node[nameKey] && node[nameKey].toLowerCase().indexOf(_keywords.toLowerCase())!=-1) {
				if(isHighLight){  //如果高亮，对文字进行高亮处理
					//创建一个新变量newKeywords,不影响_keywords在下一个节点使用
					//对_keywords中的元字符进行处理,否则无法在replace中使用RegExp
					//process the meta characters in _keywords thus the RegExp can be correctly used in str.replace
					var newKeywords = _keywords.replace(rexMeta,function(matchStr){
						//对元字符做转义处理
						return '\\' + matchStr;
					});
					node.oldname = node[nameKey]; //缓存原有名称用于恢复
					var rexGlobal = new RegExp(newKeywords, 'gi');//'g' for global,'i' for ignore case
					//use replace(RegExp,replacement) since replace(/substr/g,replacement) cannot be used here
					node[nameKey] = node.oldname.replace(rexGlobal, function(originalText){
						//highlight the matching words in node name
						var highLightText =
							'<span style="color: whitesmoke;background-color: darkred;">'
							+ originalText
							+'</span>';
						return 	highLightText;					
					});
					zTreeObj.updateNode(node); //update node for modifications take effect
				}
				zTreeObj.showNode(node);//show node with matching keywords
				return true; //return true and show this node
			}
			
			zTreeObj.hideNode(node); // hide node that not matched
			return false; //return false for node not matched
		}
		
		var nodesShow = zTreeObj.getNodesByFilter(filterFunc); //get all nodes that would be shown
		processShowNodes(nodesShow, _keywords);//nodes should be reprocessed to show correctly
	}
	
	/**
	 * reprocess of nodes before showing
	 */
	function processShowNodes(nodesShow,_keywords){
		if(nodesShow && nodesShow.length>0){
			//process the ancient nodes if _keywords is not blank
			if(_keywords.length>0){ 
				$.each(nodesShow, function(n,obj){
					var pathOfOne = obj.getPath();//get all the ancient nodes including current node
					if(pathOfOne && pathOfOne.length>0){ 
						//i < pathOfOne.length-1 process every node in path except self
						for(var i=0;i<pathOfOne.length-1;i++){
							zTreeObj.showNode(pathOfOne[i]); //show node 
							zTreeObj.expandNode(pathOfOne[i],true); //expand node
						}
					}
				});	
			}else{ //show all nodes when _keywords is blank and expand the root nodes
				var rootNodes = zTreeObj.getNodesByParam('level','0');//get all root nodes
				$.each(rootNodes,function(n,obj){
					zTreeObj.expandNode(obj,true); //expand all root nodes
				});
			}
		}
	}
	
	//listen to change in input element
	$(searchField).bind('input propertychange', function() {
		var _keywords = $(this).val();
		searchNodeLazy(_keywords); //call lazy load
	});

	var timeoutId = null;
  var lastKeyword = '';
	// excute lazy load once after input change, the last pending task will be cancled  
	function searchNodeLazy(_keywords) {
		if (timeoutId) { 
			//clear pending task
			clearTimeout(timeoutId);
		}
		timeoutId = setTimeout(function() {
      if (lastKeyword === _keywords) {
        return;
      }
			ztreeFilter(zTreeObj,_keywords); //lazy load ztreeFilter function 
			// $(searchField).focus();//focus input field again after filtering
      lastKeyword = _keywords;
		}, 500);
	}
}