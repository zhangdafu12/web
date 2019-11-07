var edges_path;
var edges_text;
var circle;
var nodes_text;
// var tooltip;
function create_img(divid,data){
    // console.log(divid);
	var options = {};
    options.backgroundColor = "#D1EEEE";
    options.nodesFontType = "SimSun";
    options.nodesFontSize = 20;
    options.lineFontType = "SimHei";
    options.lineFontSize = 12;
    options.lineColor = "#000000";
    options.showExamples = true;
    options.examplesX = 20;
    options.examplesY = 250;
    options.examplesFontColor = "#000000";
    var datas = data;
    var dataFilter = [];
    var backgroundColor = options.backgroundColor; //背景颜色
    var nodesFontType = options.nodesFontType; //节点字体
    var nodesFontSize = options.nodesFontSize; //节点字号
    var lineFontType = options.lineFontType; //关系字体
    var lineFontSize = options.lineFontSize; //关系字号
    var lineColor = options.lineColor; //连线颜色
    var examplesFontColor = options.examplesFontColor; //关系示例字体颜色
    var box = document.getElementById(divid);
    // var contentHeight = window.getComputedStyle(box).height;
    var contentHeight = window.screen.height;
    // contentHeight=contentHeight.substr(0,contentHeight.length-2);
    // console.log(contentHeight);
    var contentWidth = window.screen.width;
    // var contentWidth = window.getComputedStyle(box).width;
    // contentWidth=contentWidth.substr(0,contentWidth.length-2);
    // console.log(contentWidth);
    var width = contentWidth ; //画布宽
    var height = contentHeight; //画布高
    var svgChart = d3.select("svg");
    svgChart.remove();
    // var tip = $(".tooltip");
    // if(tip.length > 0){
    //     tip.remove();
    // }
    var sourceDatas = {};
    sourceDatas.links = [];

    var linkss = datas.data.relationships;

    for(var i = 0; i < linkss.length; i++){
        // debugger
        var jsonObj = {};
        jsonObj.source = linkss[i].startNode;
        jsonObj.target = linkss[i].endNode;
        jsonObj.relation = linkss[i].properties.labels[0];
        jsonObj.sourceId = "";
        jsonObj.targetId = "";
        jsonObj.sourceImg = "";
        jsonObj.targetImg = "";
        jsonObj.sourceColor = "";
        jsonObj.targetColor = "";
        jsonObj.sourceRadius = 45;
        jsonObj.targetRadius = 45;
        jsonObj.lineColor = "#0070cd";
        sourceDatas.links.push(jsonObj);
    }
    var resourceLinks = sourceDatas.links;

    if(dataFilter != undefined && dataFilter.length > 0){

        var indexArray = [];
        for(var i = 0; i < dataFilter.length; i++){
            for(var j = 0; j < resourceLinks.length; j++){
                if(resourceLinks[j].relation == dataFilter[i].relation && dataFilter[i].isShow == "false"){
                    indexArray.push(j);
                }
            }
        }
        if(indexArray.length > 0){
            var tempArray = [];
            for(var j = 0; j < resourceLinks.length; j++){
                console.log(indexArray.length,resourceLinks.length,tempArray,)
                for(var i = 0; i < indexArray.length; i++){
                    if(indexArray[i] != j){
                        if(i == indexArray.length-1){
                            tempArray.push(resourceLinks[j]);
                            break;
                        }
                        continue;
                    }else{
                        break;
                    }

                }
            }
            resourceLinks = tempArray;
        }
    }
    var links = resourceLinks;

    //关系分组
    var linkGroup = {};
    //对连接线进行统计和分组，不区分连接线的方向，只要属于同两个实体，即认为是同一组
    var linkmap = {};
    for(var i=0; i<links.length; i++){
        var key = links[i].source<links[i].target?links[i].source+':'+links[i].target:links[i].target+':'+links[i].source;
        if(!linkmap.hasOwnProperty(key)){
            linkmap[key] = 0;
        }
        linkmap[key]+=1;
        if(!linkGroup.hasOwnProperty(key)){
            linkGroup[key]=[];
        }
        linkGroup[key].push(links[i]);
    }
    //为每一条连接线分配size属性，同时对每一组连接线进行编号
    for(var i=0; i<links.length; i++){
        var key = links[i].source<links[i].target?links[i].source+':'+links[i].target:links[i].target+':'+links[i].source;
        links[i].size = linkmap[key];
        //同一组的关系进行编号
        var group = linkGroup[key];
        //给节点分配编号
        setLinkNumber(group);
    }

    //节点
    var nodes = {};
    //关系对应颜色
    var relationColor = {};
    var json_nodes = datas.data.nodes;
    json_nodes.forEach(function(node) {
        node["name"] = node.properties.name;
        node["color"] = "";
        node["image"] = "";
        node["radious"] = 45;
        nodes[node.id] = node;
    });
    for(var i = 0; i < links.length; i++){
        links[i].source = nodes[links[i].source] || (nodes[links[i].source] = {name: links[i].source,color:links[i].sourceColor,image:links[i].sourceImg,radius:links[i].sourceRadius});
        links[i].target = nodes[links[i].target] || (nodes[links[i].target] = {name: links[i].target,color:links[i].targetColor,image:links[i].targetImg,radius:links[i].targetRadius});
    }

    var sourceData = sourceDatas.links;
    for(var i = 0; i < sourceData.length; i++){
        relationColor[sourceData[i].relation]={"relation":sourceData[i].relation,"lineColor":sourceData[i].lineColor};
    }


    nodes = d3.values(nodes);
    relationColor = d3.values(relationColor);

    var examples_x = parseFloat(options.examplesX); //关系示例坐标x
    var examples_y = parseFloat(options.examplesY); //关系示例坐标y
    var examplesLength = 80;
    var examplesSize = Math.floor((width - examples_x)/examplesLength);
    var examplesRow = relationColor.length%examplesSize==0?relationColor.length/examplesSize:Math.ceil(relationColor.length/examplesSize);
    //计算关系示列位置
    for(var i = 1; i <= relationColor.length; i++){
        var num = i%examplesSize==0?examplesSize:i%examplesSize;
        relationColor[i-1].x = examples_x+(num-1)*examplesLength;
        relationColor[i-1].y = examples_y+20*Math.ceil(i/examplesSize);
        // console.log(relationColor[i-1].x, relationColor[i-1].y)
    }
      // console.log(dataFilter)
    if(dataFilter == undefined){
        dataFilter = [];
        for(var i = 0; i < relationColor.length; i++){
            dataFilter.push({"relation":relationColor[i].relation,"isShow":"true"});

        }
    }


    //绑定相连节点
    for(var i = 0; i < nodes.length; i++){
        for(var j = 0; j < links.length; j++){

            if(nodes[i].name == links[j].source.name){

                nodes[i][links[j].target.name] = {name: links[j].target.name};
            }
            if(nodes[i].name == links[j].target.name){
                nodes[i][links[j].source.name] = {name: links[j].source.name};
            }
        }
    }

    //缩放
    var curPos_x, curPos_y, mousePos_x, mousePos_y;
    var isMouseDown=false, oldScale = 0.01;
    var viewBox_x = 0, viewBox_y = 0;
    var zoom = d3.behavior.zoom()
        .scaleExtent([0.1, 10])
        .on("zoom", function () {
            // console.log(oldScale);
            // console.log(d3.event.scale);
            // console.log(oldScale / d3.event.scale);
            if (oldScale !== d3.event.scale) {
                var scale = oldScale / d3.event.scale;
                oldScale = d3.event.scale;
                viewBox_x = curPos_x - scale * (curPos_x - viewBox_x);
                viewBox_y = curPos_y - scale * (curPos_y - viewBox_y);
                svg.attr("viewBox", viewBox_x + " " + viewBox_y + " " + width / oldScale + " " + height / oldScale);
            }
        });
    var isDrag = false;
    var svg = d3.select("#"+divid).append("svg")
        .attr("viewBox", "0 -5 10 10")
        .attr("width",width)
        .attr("height",height)
        .call(zoom)
        .attr("style","background-color:" + backgroundColor);

    svg.on("dblclick",function(d){
        console.log("双击事件");
    });

    svg.on("mousedown", function () {
        if (d3.event.defaultPrevented) {
            return;
        }
        isMouseDown = true;
        mousePos_x = d3.mouse(this)[0];
        mousePos_y = d3.mouse(this)[1];
    });

    svg.on("mouseup", function () {
        if (d3.event.defaultPrevented) {
            return;
        }
        isMouseDown = false;

        if(isDrag==false){
            edges_text.style("fill-opacity",1);
            edges_path.style("opacity",1);
            circle.style("opacity",1);
            nodes_text.style("opacity",1);
            // tooltip.style("opacity",0.0);
            }
        isDrag = false;
    });

    svg.on("mousemove", function () {
        if (d3.event.defaultPrevented) {
            return;
        }

        curPos_x = d3.mouse(this)[0];
        curPos_y = d3.mouse(this)[1];
        if (isMouseDown) {
            viewBox_x = viewBox_x - d3.mouse(this)[0] + mousePos_x;
            viewBox_y = viewBox_y - d3.mouse(this)[1] + mousePos_y;
            svg.attr("viewBox", viewBox_x + " " + viewBox_y + " " + width / oldScale + " " + height / oldScale);
            isDrag = true;
        }
    });
    svg.call(zoom).on("dblclick.zoom", null);
 console.log(options,11)
    if(options.showExamples==true){
        debugger
        var examples = svg.selectAll(".examples")
            .data(relationColor)
            .enter()
            .append("svg:g")
            .attr("fill-opacity",function(d){
                for(var i = 0; i < dataFilter.length; i++){
                    if(d.relation == dataFilter[i].relation && dataFilter[i].isShow == "false"){
                        return 0.2;
                    }
                }
                return 1;
            })
            .on("click", function(d){
                for(var i = 0; i < dataFilter.length; i++){
                    if(dataFilter[i].relation == d.relation){
                        if(dataFilter[i].isShow == "true"){
                            dataFilter[i].isShow = "false";
                        }else{
                            dataFilter[i].isShow = "true";
                        }
                    }
                }
                drawChart(divid,options,datas,dataFilter);
            });
        examples.append("svg:path")
            .attr("d", function(d){
                var x1 = d.x;
                var y1 = d.y;
                var x2 = x1 + 20;
                var y2 = y1;
                return 'M'+x1+' '+y1+' L '+ x2 +' '+y2;
            })
            .style("stroke",function(d){
                if(d.lineColor == ""){
                    return lineColor;
                }else{
                    return d.lineColor;
                }
            })
            .style("stroke-width",2.5);
        examples.append("svg:text")
            .style("font-size","14px")
            .style("fill",examplesFontColor)
            .attr("x",function(d){
                if(d.relation.length > 3){

                    return d.x + 20 + 14*4/2;
                }

                return d.x + 20 + 14*d.relation.length/2;
            })
            .attr("y", function(d){

                return d.y+5;
            })
            .attr('text-anchor', "middle")
            .text(function(d){
                if(d.relation.length > 3){
                    return d.relation.substring(0,3)+"...";
                }
                return d.relation;
            })
            // .on("mouseover",function(d){
            //     tooltip.html("<span>"+d.relation+"</span>")
            //         .style("left",(d3.event.pageX)+"px")
            //         .style("top",(d3.event.pageY+20)+"px")
            //         .style("display","block")
            //         .style("position","absolute")
            //         .style("opacity",1.0);
            // })
            // .on("mouseout",function(d,i){
            //     tooltip.style("opacity",0.0);
            // });
    }



    //D3力导向布局
    var force = d3.layout.force()
        .nodes(nodes)
        .links(links)
        .size([width,height])
        .linkDistance(200)
        .charge(-1500)

        .on("start", function(){
            svg.attr("viewBox", 0 + " " + 0 + " " + 1800 + " " + 2800);
        })
        .start();


    //边
    edges_path = svg.selectAll(".edgepath")
        .data(links)
        .enter()
        .append("path")
        .attr("marker-end",function(d,i){
            var arrowMarker = svg.append("marker")
                .attr("id","arrow"+i)
                .attr("markerUnits","userSpaceOnUse")
                .attr("markerWidth","16")
                .attr("markerHeight","15")
                .attr("viewBox","0 0 12 12")
                .attr("refX",9)
                .attr("refY",0.2)
                .attr("orient","auto")
                .append("svg:path")
                .attr("d","M2,2 L10,6 L2,10 L6,6 L2,2")
                .attr("fill",function(){
                    return d.lineColor = "" ? lineColor:d.lineColor;
                });

            return "url(#arrow" + i + ")";
        })
        .style("stroke",function(d){
            return "#BBB";
        })
        .style("stroke-width",1.5)
        .on("click",function(d){
            d3.event.stopPropagation();
            edges_text.style("fill-opacity",1);
            edges_path.style("stroke-width",1.5);
            //影藏其它连线上文字
            edges_text.style("fill-opacity",function(edge){
                if(edge === d){
                    return 1;
                }
                return 0;
            });

            edges_path.style("stroke-width",function(edge){
                if(edge === d){
                    return 4;
                }
                return 1.5;
            })
        });


    //边上的文字（人物之间的关系）
    edges_text = svg.selectAll(".linetext")
        .data(links)
        .enter()
        .append("svg:g")
        .attr("class", "linetext")
        .attr("fill-opacity",1);
    edges_text.append("svg:text")
        .style("font-size",(lineFontSize+"px"))
        .style("font-family",lineFontType)
        .style("fill","#000000")
        .attr("y", ".31em")
        .attr('text-anchor', "middle")
        .text(function(d){
            return d.relation;
        });

    edges_text.insert('rect', 'text')
        .attr('width', function(d){
            return d.relation.length*lineFontSize;
        })
        .attr('height', function(d){
            return lineFontSize;
        })
        .attr("y", "-.6em")
        .attr('x', function (d) {
            return -d.relation.length*lineFontSize/2;
        })
        .style('fill', 'rgb(255, 255, 255,0)');

    // 圆形图片节点（人物头像）
    circle = svg.selectAll("circle")
        .data(nodes)
        .enter()
        .append("circle")

        .style("stroke",function(d){
            // console.log(d);
            if(d.properties.ntype=="f"){
                return "rgb(5, 87, 165)";
            }else if(d.properties.ntype=="s"){
                return "rgb(193, 67, 26)";
            }
        })
        .attr("fill", function(d,i){
            //节点图片不为空是添加背景色
            if(d.image == ""){
                if(d.color == ""){
                    // console.log(d);
                    if(d.properties.ntype=="f"){
                        return "rgb(1, 131, 254)";
                    }else if(d.properties.ntype=="s"){
                        return "rgb(242, 90, 41)";
                    }
                }
                return d.color;
            }else{
                //创建圆形图片
                var defs = svg.append("defs").attr("id", "imgdefs");
                var catpattern = defs.append("pattern")
                    .attr("id", "catpattern" + i)
                    .attr("height", 1)
                    .attr("width", 1);

                catpattern.append("image")
                    .attr("width", d.radius*2)
                    .attr("height", d.radius*2)
                    .attr("xlink:href", d.image);

                return "url(#catpattern" + i + ")";
            }

        })
        .style("stroke-width","2px")
        .attr("r", function(d){
            // console.log(d);
            return d.radious;
        })
        .attr("title",function(d){
            // console.log(d);
            return d.name;
        })

        .on("click",function(d,i){
            d3.event.stopPropagation();
            edges_text.style("fill-opacity",1);
            edges_path.style("opacity",1);
            circle.style("opacity",1);
            nodes_text.style("opacity",1);
            // tooltip.style("opacity",0.0);
            //影藏其它连线上文字
            edges_text.style("fill-opacity",function(edge){
                if( edge.source === d || edge.target === d ){
                    return 1;
                }
                if( edge.source !== d && edge.target !== d ){
                    return 0;
                }
            });
            //其它节点亮度调低
            circle.style("opacity",function(edge){
                var v = d.name;
                if( edge.name == v || (edge[v] != undefined &&  edge[v].name == v)){
                    return 1;
                }else{
                    return 0.2;
                }
            });
            circle.style("stroke",function(edge){
                var v = d.name;
                if( edge.name == v){
                    if(edge.properties.ntype=="f"){
                        return "rgb(5, 87, 165,0.5)";
                    }else if(edge.properties.ntype=="s"){
                        return "rgb(193, 67, 26,0.5)";
                    }
                }else{
                    if(edge.properties.ntype=="f"){
                        return "rgb(5, 87, 165)";
                    }else if(edge.properties.ntype=="s"){
                        return "rgb(193, 67, 26)";
                    }
                }
            });
            circle.style("stroke-width",function(edge){
                var v = d.name;
                if( edge.name == v){
                    return "8px";
                }else{
                    return "2px";
                }
            });
            //其他连先亮度调低
            edges_path.style("opacity",function(edge){
                if( edge.source === d || edge.target === d ){
                    return 1;
                }
                if( edge.source !== d && edge.target !== d ){
                    return 0.2;
                }
            });
            //其他节点文字亮度调低
            nodes_text.style("opacity",function(edge){
                var v = d.name;
                if( edge.name == v || (edge[v] != undefined &&  edge[v].name == v)){
                    return 1;
                }else{
                    return 0.2;
                }
            })

        })
        .on("dbclick",function(d,i){

        })
        .call(force.drag);

    // tooltip = d3.select("body").append("div")
    //     .attr("class","tooltip")
    //     .attr("opacity",0.0);


    nodes_text = svg.selectAll(".nodetext")
        .data(nodes)
        .enter()
        .append("text")
        .style("font-size",(nodesFontSize+"px"))
        .style("font-family",nodesFontType)
        .attr('x',function(d){
            var name = d.name;
            //如果小于四个字符，不换行
            if(name.length < 4){
                d3.select(this).append('tspan')
                    .attr("dx",-nodesFontSize*(name.length/2))
                    .text(function(){return name;});
            }else if(name.length >= 4 && name.length <= 6) {
                var top=d.name.substring(0,3);
                var bot=d.name.substring(3,name.length);

                d3.select(this).append('tspan')
                    .attr("dx",-nodesFontSize*1.5)
                    .attr("dy",-nodesFontSize*0.5)
                    .text(function(){return top;});

                d3.select(this).append('tspan')
                    .attr("dx",-(nodesFontSize*name.length/2))
                    .attr("dy",nodesFontSize)
                    .text(function(){return bot;});
            }else if(name.length > 7){
                var top=d.name.substring(0,3);
                var mid=d.name.substring(3,6);
                var bot=d.name.substring(6,name.length);

                d3.select(this).append('tspan')
                    .attr("dx",-nodesFontSize*1.5)
                    .attr("dy",-nodesFontSize*0.5)
                    .text(function(){return top;});


                d3.select(this).append('tspan')
                    .attr("dx",-nodesFontSize*3)
                    .attr("dy",nodesFontSize)
                    .text(function(){return mid;});

                d3.select(this).append('tspan')
                    .attr("dx",-nodesFontSize*2)
                    .attr("dy",nodesFontSize)
                    .text(function(){return "...";});
            }
        })
        .on("click",function(d,i){
            d3.event.stopPropagation();
            edges_text.style("fill-opacity",1);
            edges_path.style("opacity",1);
            circle.style("opacity",1);
            nodes_text.style("opacity",1);
            // tooltip.style("opacity",0.0);

            //影藏其它连线上文字
            edges_text.style("fill-opacity",function(edge){


                if( edge.source === d || edge.target === d ){
                    return 1;
                }
                if( edge.source !== d && edge.target !== d ){
                    return 0;
                }
            });
            //其他节点亮度调低
            circle.style("opacity",function(edge){
                var v = d.name;
                if( edge.name == v || (edge[v] != undefined &&  edge[v].name == v)){
                    return 1;
                }else{
                    return 0.2;
                }
            });
            circle.style("stroke",function(edge){
                var v = d.name;
                if( edge.name == v){
                    if(edge.properties.ntype=="f"){
                        return "rgb(5, 87, 165,0.5)";
                    }else if(edge.properties.ntype=="s"){
                        return "rgb(193, 67, 26,0.5)";
                    }
                }else{
                    if(edge.properties.ntype=="f"){
                        return "rgb(5, 87, 165)";
                    }else if(edge.properties.ntype=="s"){
                        return "rgb(193, 67, 26)";
                    }
                }
            });
            circle.style("stroke-width",function(edge){
                var v = d.name;
                if( edge.name == v){
                    return "8px";
                }else{
                    return "2px";
                }
            });

            //其他连线亮度调低
            edges_path.style("opacity",function(edge){
                if( edge.source === d || edge.target === d ){
                    return 1;
                }
                if( edge.source !== d && edge.target !== d ){
                    return 0.2;
                }
            });
            //其他节点文字亮度调低
            nodes_text.style("opacity",function(edge){
                var v = d.name;
                if( edge.name == v || (edge[v] != undefined &&  edge[v].name == v)){
                    return 1;
                }else{
                    return 0.2;
                }
            });

        })
        .on("mouseover",function(d){
            // tooltip.html("<span>"+d.name+"</span>")
            //     .style("left",(d3.event.pageX)+"px")
            //     .style("top",(d3.event.pageY+20)+"px")
            //     .style("display","block")
            //     .style("opacity",1.0);
        })
        .on("mouseout",function(d,i){
            //显示连线上的文字
            // tooltip.style("opacity",0.0);
        }
        )
        .call(force.drag);

    var drag = force.drag()
        .on("dragstart",function(d,i){
            d3.event.sourceEvent.stopPropagation();
            d.fixed = true;    //拖拽开始后设定被拖拽对象为固定
        })
        .on("dragend",function(d,i){
        })
        .on("drag",function(d,i){
        });

    //力学图运动开始时
    force.on("start", function(){

    });

    //力学图运动结束时
    force.on("end", function(){
        for (var node in nodes){
            nodes[node].fixed = true;
        }
    });

    force.on("tick", function(){
        // //限制结点的边界
        edges_path.attr("d", function(d) {
            var tan = Math.abs((d.target.y - d.source.y)/(d.target.x - d.source.x)); //圆心连线tan值
            var x1 = d.target.x - d.source.x > 0 ? Math.sqrt(d.sourceRadius*d.sourceRadius/(tan*tan + 1)) + d.source.x :
                d.source.x - Math.sqrt(d.sourceRadius*d.sourceRadius/(tan*tan + 1)); //起点x坐标
            var y1 = d.target.y - d.source.y > 0 ? Math.sqrt(d.sourceRadius*d.sourceRadius*tan*tan/(tan*tan + 1)) + d.source.y :
                d.source.y - Math.sqrt(d.sourceRadius*d.sourceRadius*tan*tan/(tan*tan + 1)); //起点y坐标
            var x2 = d.target.x - d.source.x > 0 ? d.target.x - Math.sqrt(d.targetRadius*d.targetRadius/(1+tan*tan)) :
                d.target.x + Math.sqrt(d.targetRadius*d.targetRadius/(1+tan*tan));//终点x坐标
            var y2 = d.target.y - d.source.y > 0 ? d.target.y - Math.sqrt(d.targetRadius*d.targetRadius*tan*tan/(1+tan*tan)) :
                d.target.y + Math.sqrt(d.targetRadius*d.targetRadius*tan*tan/(1+tan*tan));//终点y坐标
            if(d.target.x - d.source.x == 0 || tan == 0){ //斜率无穷大的情况或为0时
                y1 = d.target.y - d.source.y > 0 ? d.source.y + d.sourceRadius:d.source.y - d.sourceRadius;
                y2 = d.target.y - d.source.y > 0 ? d.target.y - d.targetRadius:d.target.y + d.targetRadius;
            }
            if(d.linknum==0){//设置编号为0的连接线为直线，其他连接线会均分在两边
// console.log(d.size)
                d.x_start = x1;
                d.y_start = y1;
                d.x_end = x2;
                d.y_end = y2;
                return 'M'+x1+' '+y1+' L '+ x2 +' '+y2;
            }
            var a = d.sourceRadius > d.targetRadius ? d.targetRadius*d.linknum/3 : d.sourceRadius*d.linknum/3;
            var xm =d.target.x - d.source.x > 0 ? d.source.x + Math.sqrt((d.sourceRadius*d.sourceRadius-a*a)/(1+tan*tan)):
                d.source.x - Math.sqrt((d.sourceRadius*d.sourceRadius-a*a)/(1+tan*tan));
            var ym =d.target.y - d.source.y > 0 ? d.source.y + Math.sqrt((d.sourceRadius*d.sourceRadius-a*a)*tan*tan/(1+tan*tan)):
                d.source.y - Math.sqrt((d.sourceRadius*d.sourceRadius-a*a)*tan*tan/(1+tan*tan));
            var xn =d.target.x - d.source.x > 0 ? d.target.x - Math.sqrt((d.targetRadius*d.targetRadius-a*a)/(1+tan*tan)):
                d.target.x + Math.sqrt((d.targetRadius*d.targetRadius-a*a)/(1+tan*tan));
            var yn =d.target.y - d.source.y > 0 ? d.target.y - Math.sqrt((d.targetRadius*d.targetRadius-a*a)*tan*tan/(1+tan*tan)):
                d.target.y + Math.sqrt((d.targetRadius*d.targetRadius-a*a)*tan*tan/(1+tan*tan));
            if(d.target.x - d.source.x == 0 || tan == 0){//斜率无穷大或为0时
                ym = d.target.y - d.source.y > 0 ? d.source.y + Math.sqrt(d.sourceRadius*d.sourceRadius-a*a):d.source.y - Math.sqrt(d.sourceRadius*d.sourceRadius-a*a);
                yn = d.target.y - d.source.y > 0 ? d.target.y - Math.sqrt(d.targetRadius*d.targetRadius-a*a):d.target.y + Math.sqrt(d.targetRadius*d.targetRadius-a*a);
            }

            var k = (x1-x2)/(y2-y1);//连线垂线的斜率
            var dx = Math.sqrt(a*a/(1+k*k)); //相对垂点x轴距离
            var dy = Math.sqrt(a*a*k*k/(1+k*k)); //相对垂点y轴距离
            if((y2-y1) == 0){
                dx = 0;
                dy = Math.sqrt(a*a);
            }
            if(a > 0){
                var xs = k > 0 ? xm - dx : xm + dx;
                var ys = ym - dy;
                var xt = k > 0 ? xn - dx : xn + dx;
                var yt = yn - dy;
            }else{
                var xs = k > 0 ? xm + dx : xm - dx;
                var ys = ym + dy;
                var xt = k > 0 ? xn + dx : xn - dx;
                var yt = yn + dy;
            }
            //记录连线起始和终止坐标，用于定位线上文字
            d.x_start = xs;
            d.y_start = ys;
            d.x_end = xt;
            d.y_end = yt;
            return 'M'+xs+' '+ys+' L '+ xt +' '+yt;
        });

        //更新连接线上文字的位置
        edges_text.attr("transform", function (d) {
            return "translate(" + (d.x_start + d.x_end)/2 + "," + (d.y_start + d.y_end)/2 + ")" + " rotate(" + Math.atan((d.y_end - d.y_start) / (d.x_end - d.x_start)) * 180 / Math.PI + ")";
        });

        //更新结点图片和文字
        circle.attr("cx",function(d){ return d.x });
        circle.attr("cy",function(d){ return d.y });
        nodes_text.attr("x",function(d){ return d.x });
        nodes_text.attr("y",function(d){ return d.y });
    });
//连接线
function setLinkNumber(group){

    if(group.length==0) return;
    if(group.length==1){
        group[0].linknum = 0;
        return;
    }
    var maxLinkNumber = group.length%2==0?group.length/2:(group.length-1)/2;
    if(group.length%2==0){
        var startLinkNum = -maxLinkNumber + 0.5;
        for(var i = 0;i<group.length;i++){
            group[i].linknum = startLinkNum++;
        }
    }else{
        var startLinkNum = -maxLinkNumber;
        for(var i = 0;i<group.length;i++){
            group[i].linknum = startLinkNum++;
        }
    }
}
}

