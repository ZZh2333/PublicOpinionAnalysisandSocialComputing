// ;
// var w=window.innerWidth|| document.documentElement.clientWidth|| document.body.clientWidth;
// var h=window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;
//             w=w*0.75;
//             h=h*0.80;
//             var fill = d3.scale.category20();
//             var words=new Array({{wordcount}});
//             {% for wc in wordcloud %}
//             words[{{loop.index-1}}]={text:"{{wc[1]}}",size:"{{wc[0]/3}}"};
//             {% endfor %}
//             var wc=d3.layout.cloud()
//                     .size([w, 300])
//                     .words(words)
//                     .padding(5)
//                     .rotate(function() { return ~~(Math.random() * 2) * 90; })
//                     .font("Impact")
//                     .fontSize(function(d) { return d.size; })
//                     .on("end", draw)
//                     .start();

//             function draw(words) {
//             d3.select("div.card-action").append("svg")
//                 .attr("width", w)
//                 .attr("height", 300)
//                 .append("g")
//                 .attr("transform", "translate("+w/2+",150)")
//                 .selectAll("text")
//                 .data(words)
//                 .enter()
//                 .append("a")
//                 .attr("xlint:href",function(d){
//                                 return "/wordcloud/cucnews?wanted="+d.text;
//                         })
//                 .append("text")
//                 .style("font-size", function(d) { return d.size + "px"; })
//                 .style("font-family", "Impact")
//                 .style("fill", function(d, i) { return fill(i); })
//                 .attr("text-anchor", "middle")
//                 .attr("transform", function(d) {
//                     return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
//                 })
//                 .text(function(d) { return d.text; });
//             }
