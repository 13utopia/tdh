<?php
if (!defined('ABSPATH')) {
    exit;
}

function google_rank_register_settings() {
    register_setting('google_rank_options_group', 'google_rank_option_name');
}
add_action('admin_init', 'google_rank_register_settings');

function google_rank_settings_link($links) {
    $settings_link = '<a href="options-general.php?page=google-rank">Settings</a>';
    array_unshift($links, $settings_link);
    return $links;
}
add_filter('plugin_action_links_' . plugin_basename(__FILE__), 'google_rank_settings_link');
?>