<?php
if (!defined('ABSPATH')) {
    exit;
}

function google_rank_example_function() {
    $current_user = wp_get_current_user();
    if ($current_user->exists()) {
        update_user_meta($current_user->ID, 'google_rank_last_visit', current_time('mysql'));
    }
}
add_action('wp_footer', 'google_rank_example_function');

function google_rank_add_custom_post_type() {
    register_post_type('google_rank_type', array(
        'labels' => array('name' => __('Google Rank Type')),
        'public' => true,
        'has_archive' => true,
    ));
}
add_action('init', 'google_rank_add_custom_post_type');
?>