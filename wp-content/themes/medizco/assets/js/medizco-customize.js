jQuery(document).ready(function ($) {
  "use strict";

  if ($(".xs_header_builder_select").length > 0) {
    $(".xs_header_builder_select")
      .on("change", function () {
        let id = $(this).val(),
          admin_url = admin_url_object.admin_url + id;
        $(".xs_builder_edit_link").attr("href", admin_url);
      })
      .trigger("change");
  }

  if ($("#customize-theme-controls").length > 0) {
    let arr = ["header_builder_enable", "footer_builder_enable"];
    arr.forEach((element) => {
      $(".customize-control").each(function () {
        let target_value = element,
          parents = $(this).parents(".accordion-section-content");
        var str = `customize-control-${target_value}`;
        function customizer_value_dynamically_update(
          current,
          type,
          value,
          defaultClass
        ) {
          if (type === "change") {
            if (value === '"yes"') {
              $(parents).children().css("display", "list-item");
            } else if (value === '"no"') {
              $(parents).children().not(`.section-meta`).css("display", "none");
              defaultClass.css("display", "list-item");
              if (str.includes(target_value)) {
                $(parents).children(`#${str}`).css("display", "block");
              }
            }
          } else {
            let checkbox_target = current.find(
              `#fw-option-${target_value}--checkbox`
            );
            let checkbox_target_value = checkbox_target.val();

            if (checkbox_target_value === '"yes"') {
              $(parents)
                .children()
                .not(
                  `.section-meta, #customize-control-theme_header_default_settings, #customize-control-theme_footer_default_settings`
                )
                .css("display", "none");
              if (str.includes(target_value)) {
                $(parents).children(`#${str}`).css("display", "block");
              }
            } else if (checkbox_target_value === '"no"') {
              $(parents).children().css("display", "list-item");
            }
          }
        }
        customizer_value_dynamically_update($(this));

        $(this)
          .find(`#fw-option-${target_value}--checkbox`)
          .on("change", function (e) {
            customizer_value_dynamically_update(
              $(this),
              e.type,
              $(this).val(),
              $(this)
                .parents(".accordion-section-content")
                .find(".fw-option-type-multi-picker-dynamic-container")
                .parents(".customize-control")
            );
          });
      });
    });
  }
});
