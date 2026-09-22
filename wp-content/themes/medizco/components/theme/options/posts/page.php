<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * metabox options for pages
 */

$options = array(
	'settings-page' => array(
		'title'		 => esc_html__( 'Page Settings', 'medizco' ),
		'type'		 => 'box',
		'priority'	 => 'high',
		'options'	 => array(
			'header_title'	 => array(
				'type'	 => 'text',
				'label'	 => esc_html__( 'Banner Title', 'medizco' ),
				'desc'	 => esc_html__( 'Add your Page hero title', 'medizco' ),
			),
			'header_image'	 => array(
				'label'	 => esc_html__( 'Banner Image', 'medizco' ),
				'desc'	 => esc_html__( 'Upload a page header image', 'medizco' ),
				'type'	 => 'upload'
            ),
			'header_bg_image'	 => array(
				'label'	 => esc_html__( 'Banner Background Image', 'medizco' ),
				'desc'	 => esc_html__( 'Upload a page header background image', 'medizco' ),
				'type'	 => 'upload'
            ),
        ),
	),
);
