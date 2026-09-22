<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * options for wp customizer
 * section name format: medizco_section_{section name}
 */
$options = [
	'medizco_section_theme_settings' => [
		'title'				 => esc_html__( 'Theme settings', 'medizco' ),
		'options'			 => Blo_Theme_Includes::_customizer_options(),
		'wp-customizer-args' => [
			'priority' => 1,
		],
	],
];
