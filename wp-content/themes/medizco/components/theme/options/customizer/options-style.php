<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: general
 */
$options =[
    'style_settings' => [
            'title'		 => esc_html__( 'Style settings', 'medizco' ),
            'options'	 => [
                'style_body_bg' => [
                    'label'	        => esc_html__( 'Body background', 'medizco' ),
                    'desc'	           => esc_html__( 'Site\'s main background color.', 'medizco' ),
                    'type'	           => 'color-picker',
                 ],

                'style_primary' => [
                    'label'	        => esc_html__( 'Primary color', 'medizco' ),
                    'desc'	           => esc_html__( 'Site\'s main color.', 'medizco' ),
                    'type'	           => 'color-picker',
                ],

                'secondary_color' => [
                    'label'	        => esc_html__( 'Secondary color', 'medizco' ),
                    'desc'	           => esc_html__( 'Secondary color.', 'medizco' ),
                    'type'	           => 'color-picker',
                ],
                
                'title_color' => [
                'label'	        => esc_html__( 'Title color', 'medizco' ),
                'desc'	        => esc_html__( 'Blog title color.', 'medizco' ),
                'type'	        => 'color-picker',
                ],

                'body_font'    => array(
                    'type' => 'typography-v2',
                    'label' => esc_html__('Body Font', 'medizco'),
                    'desc'  => esc_html__('Choose the typography for the title', 'medizco'),
                    'value' => array(
                        'family' => 'Roboto',
                        'size'  => '15',
                        'font-weight' => '400',
                    ),
                    'components' => array(
                        'family'         => true,
                        'size'           => true,
                        'line-height'    => false,
                        'letter-spacing' => false,
                        'color'          => false,
                        'font-weight'    => true,
                    ),
                ),
                
                'heading_font_one'	 => [
                    'type'		 => 'typography-v2',
                    'value'		 => [
                        'family'		 => 'Exo',
                        'size'  => '',
                        'font-weight' => '700',
                    ],
                    'components' => [
                        'family'         => true,
                        'size'           => true,
                        'line-height'    => false,
                        'letter-spacing' => false,
                        'color'          => false,
                        'font-weight'    => true,
                    ],
                    'label'		 => esc_html__( 'Heading H1 and H2 Fonts', 'medizco' ),
                    'desc'		    => esc_html__( 'This is for heading google fonts', 'medizco' ),
                ],

                'heading_font_two'	 => [
                    'type'		    => 'typography-v2',
                    'value'		 => [
                        'family'		  => 'Exo',
                        'size'        => '',
                        'font-weight' => '700',
                    ],
                    'components' => [
                        'family'         => true,
                        'size'           => true,
                        'line-height'    => false,
                        'letter-spacing' => false,
                        'color'          => false,
                        'font-weight'    => true,
                    ],
                    'label'		 => esc_html__( 'Heading H3 Fonts', 'medizco' ),
                    'desc'		    => esc_html__( 'This is for heading google fonts', 'medizco' ),
                ],

                'heading_font_three'	 => [
                    'type'		    => 'typography-v2',
                    'value'		 => [
                        'family'		  => 'Exo',
                        'size'        => '',
                        'font-weight' => '700',
                    ],
                    'components' => [
                        'family'         => true,
                        'size'           => true,
                        'line-height'    => false,
                        'letter-spacing' => false,
                        'color'          => false,
                        'font-weight'    => true,
                    ],
                    'label'		 => esc_html__( 'Heading H4 Fonts', 'medizco' ),
                    'desc'		    => esc_html__( 'This is for heading google fonts', 'medizco' ),
                ],
            ],
        ],
    ];