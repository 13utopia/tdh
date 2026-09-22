<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * register required plugins
 */

function medizco_register_required_plugins() {
	$plugins	 = array(
		array(
			'name'		 => __( 'Unyson Custom', 'medizco' ),
			'slug'       => 'unyson',
            'required'   => true,
            'version'    => '2.8.0',
            'source'     =>  MEDIZCO_GLOBAL_UNYSON . '/unyson.zip',
		),
		array(
			'name'		 => __( 'Elementor', 'medizco' ),
			'slug'		 => 'elementor',
			'required'	 => true,
		),
		array(
			'name'		 => __( 'ElementsKit Lite', 'medizco' ),
			'slug'		 => 'elementskit-lite',
			'required'	 => true,
		),
		array(
			'name'		 => __( 'MetForm', 'medizco' ),
			'slug'		 => 'metform',
			'required'	 => true,
		),
		array(
			'name'		 => __( 'Corona Virus Data', 'medizco' ),
			'slug'		 => 'corona-virus-data',
			'required'	 => true,
		),
		array(
			'name'		 => __( 'Medizco Essentials', 'medizco' ),
			'slug'		 => 'medizco-essential',
			'required'	 => true,
			'version'	 => '1.6',
      		'source'	 => MEDIZCO_REMOTE_CONTENT . '/plugins/medizco-essential.zip',
		),
		array(
			'name'		 => __( 'Slider Revolution', 'medizco' ),
			'slug'		 => 'revslider',
			'required'	 => true,
			'version'	 => '6.6.14',
			'source'	 => MEDIZCO_REMOTE_CONTENT . '/plugins/revslider.zip',
		),
		array(
			'name'		 => __( 'Timetable and Event Schedule', 'medizco' ),
			'slug'		 => 'mp-timetable',
			'version'	 => '2.3.19',
			'source'	 => MEDIZCO_REMOTE_CONTENT . '/plugins/mp-timetable.zip',
		),
		array(
			'name'		 => __( 'Woocommerce', 'medizco' ),
			'slug'		 => 'woocommerce',
			'required'	 => true,
		),
		array(
            'name'		 => esc_html__( 'GetGenie – Conversion-Friendly & SEO-Optimized Content with AI Magic', 'medizco' ),
            'slug'		 => 'getgenie',
        ),
	);


	$config = array(
		'id'			 => 'medizco', // Unique ID for hashing notices for multiple instances of TGMPA.
		'default_path'	 => '', // Default absolute path to bundled plugins.
		'menu'			 => 'medizco-install-plugins', // Menu slug.
		'parent_slug'	 => 'themes.php', // Parent menu slug.
		'capability'	 => 'edit_theme_options', // Capability needed to view plugin install page, should be a capability associated with the parent menu used.
		'has_notices'	 => true, // Show admin notices or not.
		'dismissable'	 => true, // If false, a user cannot dismiss the nag message.
		'dismiss_msg'	 => '', // If 'dismissable' is false, this message will be output at top of nag.
		'is_automatic'	 => false, // Automatically activate plugins after installation or not.
		'message'		 => '', // Message to output right before the plugins table.
	);

	tgmpa( $plugins, $config );
}

add_action( 'tgmpa_register', 'medizco_register_required_plugins' );
