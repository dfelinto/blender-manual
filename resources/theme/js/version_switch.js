(function() {//switch: v1.2
"use strict";

var versionsFileUrl = "https://docs.blender.org/versions.json"

var all_versions;
var all_langs = {
	"en": "English",
	"ar": "&#1575;&#1614;&#1604;&#1618;&#1593;&#1614;&#1585;&#1614;&#1576;&#1616;&#1610;&#1614;&#1617;&#1577;&#1615;",
	"de": "Deutsch",
	"es": "Espa&ntilde;ol",
	"fi": "Suomeksi",
	"fr": "Fran&ccedil;ais",
	"id": "Bahasa Indonesia",
	"it": "Italiano",
	"ja": "&#x65E5;&#x672C;&#x8A9E;",
	"ko": "&#xD55C;&#xAD6D;&#xC5B4;",
	"nb": "Norsk Bokm&#x00E5;l",
	"pt": "Portugu&ecirc;s",
	"ru": "&#x3A1;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;",
	"sk": "Sloven&#269;ina",
	"sl": "Sloven&#353;&#269;ina",
	"sr": "&#1089;&#1088;&#1087;&#1089;&#1082;&#1080;",
	"uk": "Ukra&#1111;na",
	"vi": "Ti&#x1EBF;ng Vi&#x1EC7;t",
	"zh-hans": "&#x4E2D;&#x6587;(&#x7B80;&#x4F53;)",
	"zh-hant": "&#x4E2D;&#x6587;(&#x7E41;&#x9AD4;)",
};

var Popover=function(){
function Popover(id){
	this.isOpen=false;
	this.type = (id === "version-popover");
	this.$btn = $('#' + id);
	this.$dialog = this.$btn.next();
	this.$list = this.$dialog.children("ul");
	this.sel = null;
	this.beforeInit();
}

Popover.prototype={
beforeInit: function() {
	var that=this;
	this.$btn.on("click", function(e){that.init();e.preventDefault();e.stopPropagation();});
	this.$btn.on("keydown", function(e) { if(that.btnKeyFilter(e)){that.init();e.preventDefault();e.stopPropagation();} });
},
init: function() {
	this.$btn.off("click");
	this.$btn.off("keydown");

	if(all_versions === undefined) {
		this.$btn.addClass("wait");
		this.loadVL(this);
	} else {
		this.afterLoad();
	}
},
loadVL: function(that) {
	$.getJSON(versionsFileUrl, function(data) {
		all_versions = data;
		that.afterLoad();
		return true;
	})
	.fail( function() {
		console.log("Version Switch Error: versions.json could not be loaded.");
		that.$btn.addClass("disabled");
		return false;
	});
},
afterLoad: function() {
	var release = DOCUMENTATION_OPTIONS.VERSION;
	const m = release.match(/\d\.\d+/g);
	if (m) {release = m[0];}
	var lang = DOCUMENTATION_OPTIONS.LANGUAGE;
	if(!lang || lang === "None" || lang === "") {lang = "en";}

	this.warnOld(release, all_versions);

	var version = this.getNamed(release);
	var list = this.buildList(version, lang);

	this.$list.children(":first-child").remove();
	this.$list.append(list);
	var that = this;
	this.$list.on("keydown", function(e) {that.keyMove(e);});

	this.$btn.removeClass("wait");
	this.btnOpenHandler();
	this.$btn.on("mousedown", function(e){that.btnOpenHandler(); e.preventDefault()});
	this.$btn.on("keydown", function(e){ if(that.btnKeyFilter(e)){that.btnOpenHandler();} });
},
warnOld: function(release, all_versions) {
	// Note this is effectively disabled now, two issues must fixed:
	// * versions.js does not contain a current entry, because that leads to
	//   duplicate version numbers in the menu. These need to be deduplicated.
	// * It only shows the warning after opening the menu to switch version
	//   or language, when versions.js is loaded. This is too late to be useful.
	var current = all_versions.current
	if (!current) {
		//console.log("Version Switch Error: no 'current' in version.json.");
		return;
	}
	const m = current.match(/\d\.\d+/g);
	if (m) {current = parseFloat(m[0]);}
	if (release < current) {
		var currentURL = window.location.pathname.replace(release, current);
		var warning = $(
			'<div class="admonition warning"> ' +
			'<p class="first admonition-title">Note</p> ' +
			'<p class="last"> ' +
			'You are not using the most up to date version of the documentation. ' +
			'<a href="#"></a> is the newest version.' +
			'</p>' +
			'</div>');

		warning
			.find('a')
			.attr('href', currentURL)
			.text(current);

		var body = $("div.body");
		if (!body.length) {body = $("div.document");}
		body.prepend(warning);
	}
},
buildList: function(v, l) {
	var url = new URL(window.location.href);
	let pathSplit = ["", "manual", l, v];
	if (url.pathname.startsWith("/manual/")) {
		pathSplit.append(url.pathname.split('/').slice(4).join('/'));
	} else {
		pathSplit.append(url.pathname.substring(1));
	}
	if(this.type) {
		var dyn = all_versions;
		var cur = v;
	} else {
		var dyn = all_langs;
		var cur = l;
	}
	var buf = [];
	var that=this;
	$.each(dyn, function(ix, title) {
		buf.push("<li");
		if (ix === cur) {
			buf.push(' class="selected" tabindex="-1" role="presentation"><span tabindex="-1" role="menuitem" aria-current="page">' + title + '</spanp></li>');
		} else {
			pathSplit[2 + that.type] = ix;
			var href = new URL(url);
			href.pathname = pathSplit.join('/');
			buf.push(' tabindex="-1" role="presentation"><a href ="' + href + '" tabindex="-1">' + title + '</a></li>');
		}
	});
	return buf.join('');
},
getNamed: function(v) {
	$.each(all_versions, function(ix, title) {
		if (ix === "dev" || ix === "latest") {
			var m = title.match(/\d\.\d[\w\d\.]*/)[0];
			if (parseFloat(m) == v) {
				v = ix;
				return false;
			}
		}
	});
	return v;
},
dialogToggle: function(speed) {
	var wasClose = !this.isOpen;
	var that=this;
	if(!this.isOpen) {
		this.$btn.addClass("version-btn-open");
		this.$btn.attr("aria-pressed", true);
		this.$dialog.attr("aria-hidden", false);
		this.$dialog.fadeIn(speed, function() {
			that.$btn.parent().on("focusout", function(e) {that.focusoutHandler(); e.stopImmediatePropagation();})
			that.$btn.parent().on("mouseleave", function(e){that.mouseoutHandler(); e.stopImmediatePropagation();});
		});
		this.isOpen = true;
	} else {
		this.$btn.removeClass("version-btn-open");
		this.$btn.attr("aria-pressed", false);
		this.$dialog.attr("aria-hidden", true);
		this.$btn.parent().off("focusout");
		this.$btn.parent().off("mouseleave");
		this.$dialog.fadeOut(speed, function() {
			if (this.$sel) {this.$sel.attr("tabindex", -1);}
			that.$btn.attr("tabindex", 0);
			if(document.activeElement !== null && document.activeElement !== document && document.activeElement !== document.body) {
				that.$btn.focus();
			}
		});
		this.isOpen = false;
	}

	if(wasClose) {
		if (this.$sel) {this.$sel.attr("tabindex", -1);}
		if(document.activeElement !== null && document.activeElement !== document && document.activeElement !== document.body) {
			var $nw = this.listEnter();
			$nw.attr("tabindex", 0);
			$nw.focus();
			this.$sel = $nw;
		}
	}
},
btnOpenHandler: function() {
	this.dialogToggle(300);
},
focusoutHandler: function() {
	var list = this.$list;
	var that = this;
	setTimeout(function() {
		if (list.find(":focus").length === 0) {
			that.dialogToggle(200);
		}
	}, 200);
},
mouseoutHandler: function() {
	this.dialogToggle(200);
},
btnKeyFilter: function(e) {
	if (e.ctrlKey || e.shiftKey) {return false;}
	if(e.key === " " || e.key === "Enter" || (e.key === "ArrowDown" && e.altKey) || e.key === "ArrowDown" || e.key === "ArrowUp") {
		return true;
	}
	return false;
},
keyMove: function(e) {
	if (e.ctrlKey || e.shiftKey) {return true;}
	var p = true;
	var $nw = $(e.target);
	switch(e.key) {
		case "ArrowUp": $nw = this.listPrev($nw); break;
		case "ArrowDown": $nw = this.listNext($nw); break;
		case "Home": $nw = this.listFirst(); break;
		case "End": $nw = this.listLast(); break;
		case "Escape": $nw = this.listExit(); break;
		case "ArrowLeft": $nw = this.listExit(); break;
		case "ArrowRight": $nw = this.listExit(); break;
		default: p = false;
	}
	if(p) {
		$nw.attr("tabindex", 0);
		$nw.focus();
		if (this.$sel) {this.$sel.attr("tabindex", -1);}
		this.$sel = $nw;
		e.preventDefault();
		e.stopPropagation();
	}
},
listPrev: function($nw) {
	if ($nw.parent().prev().length !== 0) {
		return $nw.parent().prev().children(":first-child");
	} else {
		return this.listLast();
	}
},
listNext: function($nw) {
	if ($nw.parent().next().length !== 0) {
		return $nw.parent().next().children(":first-child");
	} else {
		return this.listFirst();
	}
},
listFirst: function() {
	return this.$list.children(":first-child").children(":first-child");
},
listLast: function() {
	return this.$list.children(":last-child").children(":first-child");
},
listExit: function() {
	this.mouseoutHandler();
	return this.$btn;
},
listEnter: function() {
	return this.$list.children(":first-child").children(":first-child");
}
};
return Popover}();

$(document).ready(function() {
	var lang = DOCUMENTATION_OPTIONS.LANGUAGE;
	if(!lang || lang === "None") {lang = "en";}
	if(all_langs.hasOwnProperty(lang)) {$("#lang-popover").html(all_langs[lang]);}
	var lng_popover=new Popover("version-popover");
	var vsn_popover=new Popover("lang-popover");
});
})();
