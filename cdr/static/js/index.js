$(function(){

    function initMap(){
        var $map = $('#map'),
            state;
        $map.mapael({
            map:{
                name : "brazil",
                defaultArea : {
                    attrsHover : {
                        fill : '#242424',
                        animDuration : 100
                    },
                    tooltip: {
                        content: function(){
                            return '<strong>' + state + '</strong>';
                        }
                    },
                    eventHandlers: {
                        mouseover: function(e, id){
                            state = id;
                        }
                    }
                },
                defaultPlot:{
                    size: 17,
                    attrs : {
                        fill : Sing.colors['brand-warning'],
                        stroke : "#fff",
                        "stroke-width" : 0,
                        "stroke-linejoin" : "round"
                    },
                    attrsHover : {
                        "stroke-width" : 1,
                        animDuration : 100
                    }
                },
                zoom : {
                    enabled : false,
                    step : 0.75
                }
            },
              plots:{
                'mg' : {
                    latitude: -19.9375,
                    longitude: -43.9265,
                    tooltip: {content : "BH"}
                },
            }
            
        });

        //ie svg height fix
        function _fixMapHeight(){
            $map.find('svg').css('height', function(){
                return $(this).attr('height') + 'px';
            });
        }

        _fixMapHeight();
        SingApp.onResize(function(){
            setTimeout(function(){
                _fixMapHeight();
            }, 100)
        });
    }

//CALENDAR HERE

    function initRickshaw(){
        "use strict";

        var seriesData = [ [], [] ];
        var random = new Rickshaw.Fixtures.RandomData(30);

        for (var i = 0; i < 1; i++) {
            random.addData(seriesData);
        }

        var graph = new Rickshaw.Graph( {
            element: document.getElementById("rickshaw"),
            height: 100,
            renderer: 'area',
            series: [
                {
                    color: '#F7653F',
                    data: seriesData[0],
                    name: 'Canais SIP'
                }, {
                    color: '#F7D9C5',
                    data: seriesData[1],
                    name: 'Users'
                }
            ]
        } );

        function onResize(){
            var $chart = $('#rickshaw');
            graph.configure({
                width: $chart.width(),
                height: 100
            });
            graph.render();

            $chart.find('svg').css({height: '100px'})
        }

        SingApp.onResize(onResize);
        onResize();


        var hoverDetail = new Rickshaw.Graph.HoverDetail( {
            graph: graph,
            xFormatter: function(x) {
                return new Date(x * 1000).toString();
            }
        } );

        setInterval( function() {
            random.removeData(seriesData);
            random.addData(seriesData);
            graph.update();

        }, 1000 );
    }

    function initAnimations(){
        $('#geo-locations-number, #percent-1, #percent-2, #percent-3').each(function(){
            $(this).animateNumber({
                number: $(this).text().replace(/ /gi, ''),
                numberStep: $.animateNumber.numberStepFactories.separator(' '),
                easing: 'easeInQuad'
            }, 1000);
        });

        $('.js-progress-animate').animateProgressBar();
    }

    function pjaxPageLoad(){
        $('.widget').widgster();
        initMap();
        initCalendar();
       // initRickshaw();
        initAnimations();
    }

    pjaxPageLoad();
    SingApp.onPageLoad(pjaxPageLoad);

});