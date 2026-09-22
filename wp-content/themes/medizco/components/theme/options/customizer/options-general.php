<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: general
 */

$options =[
    'general_settings' => [
            'title'		 => esc_html__( 'Optional settings', 'medizco' ),
            'options'	 => [
                'general_main_logo' => [
                    'label'	        => esc_html__( 'logo', 'medizco' ),
                    'desc'	           => esc_html__( 'This is default logo. Our most of the menu built with elemnetsKit header builder. Go to header settings->Header builder enable->  and click "edit header content" to change the logo.', 'medizco' ),
                    'type'	           => 'upload',
                    'image_only'      => true,
                 ],
            ],
        ],
    ];
