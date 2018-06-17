;(function ($) {
    var Score = function (obj, option) {
        var self = this;
        this.obj = obj;
        this.len = 5;
        this.eachHeight = 47;
        this.eachWidth = null;
        this.countEachImg();

        this.defaultDOM();
        this.defaultIcon = this.obj.find('.default-icon');
        this.description = this.obj.find('.score-description');

        this.defaultIcon.hover(function (e) {
            var level = $(this).attr('score-level');
            $(this).parents("[class^='score-']").children('.score-description').html(self.selectLevelDescript(level));
            var _index = $(this).parents("[class^='score-']").index() - 1;

            for (var i = 0; i < self.len; i++) {
                if (i < level) {
                    $(this).parents("[class^='score-']").find('.default-icon').eq(i).css({
                        "backgroundPositionX": -self.eachWidth * (level - 1),
                        "backgroundPositionY": -self.eachHeight * _index
                    });
                } else {
                    $(this).parents("[class^='score-']").find('.default-icon').eq(i).css({"backgroundPositionX": "right"});
                }
            }
        }, function (e) {
            var level = $(this).parent('.status-icon').attr('active-level') || 0;
            $(this).parents("[class^='score-']").children('.score-description').html(self.selectLevelDescript(level));
            var customLevel = $(this).parent('.status-icon').attr('active-level');
            for (var i = 0; i < self.len; i++) {
                if (i < parseInt(customLevel)) {
                    $(this).parents("[class^='score-']").find('.default-icon').eq(i).css({"backgroundPositionX": -self.eachWidth * (level - 1)});
                } else {
                    $(this).parents("[class^='score-']").find('.default-icon').eq(i).css({"backgroundPositionX": "right"});
                }
            }
        }).on('click', function (e) {
            e.stopPropagation();
            level = $(this).attr('score-level');
            $(this).parent('.status-icon').attr('active-level', level);
            $(this).parents("[class^='score-']").children('.score-description').html(self.selectLevelDescript(level));
        });
    };

    Score.prototype = {

        selectLevelDescript: function (n) {
            var descriptHTML = '';
            switch (parseInt(n)) {
                case 1:
                    descriptHTML = '非常不好';
                    break;
                case 2:
                    descriptHTML = '很不好';
                    break;
                case 3:
                    descriptHTML = '一般般';
                    break;
                case 4:
                    descriptHTML = '很好';
                    break;
                case 5:
                    descriptHTML = '非常好';
                    break;
                default:
                    descriptHTML = '客官觉得这篇文章怎么样呀？';
            }
            return descriptHTML;
        },
        defaultDOM: function () {
            var _scoreChild = this.obj.children("[class^='score-']");
            var _len = _scoreChild.length;
            for (var i = 0; i < _len; i++) {
                var _defaultHTML = "<div class='status-icon' icon-type='" + _scoreChild.eq(i).attr('class') + "'></div><span class='score-description' >客官觉得这篇文章怎么样呀？</span>";
                _scoreChild.eq(i).append(_defaultHTML);
            }

            var _default = this.obj.find('.status-icon');

            _default.html(this.eachChildrenDOM());
        },
        eachChildrenDOM: function () {
            var _MainHTML = "";
            for (var j = 1; j <= this.len; j++) {
                _MainHTML += "<span class='default-icon'  score-level=" + j + "></span>";
            }
            ;
            return _MainHTML;
        },
        countEachImg: function () {
            var _this_ = this;
            var img = new Image();
            _this_.obj.prepend('<img class="scoreHiddenImage" style="display:none" src="" alt="">');
            img.src = '/static/images/scoreicon.png';
            $(img).on('load error', function () {
                $('img.scoreHiddenImage').attr('src', img.src);
                each = $('img').width() / 6;
                _this_.eachWidth = each;
            })
        },
    };

    $.fn.extend({
        score: function () {
            new Score(this)
        }
    });
})(jQuery);