<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * metabox options for pages
 */
$options = array(
	'settings-page' => array(
		'title'		 => __( 'Page Settings', 'medizco' ),
		'type'		 => 'box',
		'priority'	 => 'high',
		'options'	 => array(
			'header_title'	 => array(
				'type'	 => 'text',
				'label'	 => __( 'Banner Title', 'medizco' ),
				'desc'	 => __( 'Add your Page hero title', 'medizco' ),
			),
			'header_image'	 => array(
				'label'	 => __( 'Banner Image', 'medizco' ),
				'desc'	 => __( 'Upload a page header image', 'medizco' ),
				'type'	 => 'upload'
            ),
			'header_bg_image'	 => array(
				'label'	 => __( 'Banner Background Image', 'medizco' ),
				'desc'	 => __( 'Upload a page header background image', 'medizco' ),
				'type'	 => 'upload'
            ),
        ),
	),
);
