var static_array = [{ //static list to be changed
	"full_name": "University of California, Berkeley",
	"long_acronym": "UC Berkeley",
	"short_acronym": "UCB",
	"short_name": "Berkeley",
}, {
	"full_name": "University of California, Davis",
	"long_acronym": "UC Davis",
	"short_acronym": "UCD",
	"short_name": "Davis",
}, {
	"full_name": "University of California, Irvine",
	"long_acronym": "UC Irvine",
	"short_acronym": "UCI",
	"short_name": "Irvine",
}, {
	"full_name": "University of California, Los Angeles",
	"long_acronym": "UC Los Angeles",
	"short_acronym": "UCLA",
	"short_name": "UCLA",
}, {
	"full_name": "University of California, Merced",
	"long_acronym": "UC Merced",
	"short_acronym": "UCM",
	"short_name": "Merced",
}, {
	"full_name": "University of California, Riverside",
	"long_acronym": "UC Riverside",
	"short_acronym": "UCR",
	"short_name": "Riverside",
}, {
	"full_name": "University of California, San Diego",
	"long_acronym": "UC San Diego",
	"short_acronym": "UCSD",
	"short_name": "UCSD",
}, {
	"full_name": "University of California, San Francisco",
	"long_acronym": "UC San Francisco",
	"short_acronym": "UCSF",
	"short_name": "UCSF",
}, {
	"full_name": "University of California, Santa Barbara",
	"long_acronym": "UC Santa Barbara",
	"short_acronym": "UCSB",
	"short_name": "Santa Barbara",
}, {
	"full_name": "University of California, Santa Cruz",
	"long_acronym": "UC Santa Cruz",
	"short_acronym": "UCSC",
	"short_name": "Santa Cruz",
},
];

$.noConflict();
jQuery(document).ready(function($) {
	$("#search-icon").hide();
	$(".search").focus(function() {
		$("#search-icon").show("slow");
		//console.log("This works");
	});
	$(".search").keyup(function() {
		$(".dyn-list").remove();
		if ($(".search").val() == "") {
		} else {
			var str = ($(".search").val()).toLowerCase();
			//beginning of section to be replaced
			list = [];
			var i = 0;
			console.log($(".search").val());
			static_array.forEach(function(element) {
				var should_push = false;
				//|| element.long_acronym.toLowerCase().indexOf(str) > -1 || element.short_acronym.toLowerCase().indexOf(str) > -1 || element.short_name.toLowerCase().indexOf(str) > -1
				if (element.full_name.toLowerCase().indexOf(str) > -1) {
					list.push(i);
				}
				i++;
			});
			console.log("list.length = " + list.length);
			for (var list_counter = 0; list_counter <= list.length-1; list_counter++) {
				$(".results").append("<a href='school_list/" + static_array[list[list_counter]].full_name + "' class='dyn-list' id='" + list_counter + "'>" + static_array[list[list_counter]].full_name + "</a>");
			}
			//end of section to be replaced
			$(".dyn-list").show("fast");
			$(".dyn-list").first();
		}
	});
});
