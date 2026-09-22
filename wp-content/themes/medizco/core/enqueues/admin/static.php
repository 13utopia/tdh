<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * enqueue static files: javascript and css for backend
 */




wp_enqueue_style( 'medizco-admin',  MEDIZCO_CSS . '/xs-admin.css', null,  MEDIZCO_VERSION );
if ( defined( 'FW' ) ) {
    wp_enqueue_script('medizco-customize', MEDIZCO_JS . '/medizco-customize.js', array('jquery'), MEDIZCO_VERSION, true);
}

wp_localize_script( 'medizco-customize', 'admin_url_object',array( 'admin_url' => admin_url( 'post.php?action=elementor&post=' ) ) );
