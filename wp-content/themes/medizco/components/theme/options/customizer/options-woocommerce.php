<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: banner
 */
if(!class_exists( 'WooCommerce' )) return;

$options = [
	'xs_woocommerce_setting' => [
		'title' => esc_html__('WooCommerce', 'medizco'),

		'options' => [
			'xs_woo_banner_setting' => [
                'type'        => 'popup',
                'label'       => esc_html__('Shop Banner Settings', 'medizco'),
                'popup-title' => esc_html__('Shop Banner Settings', 'medizco'),
                'button'      => esc_html__('Edit Shop Banner Button', 'medizco'),
                'size'        => 'medium', // small, medium, large
                'popup-options' => [
                    'xs_woo_show_banner' => [
                        'type'  => 'switch',
                        'label' => esc_html__( 'Show Banner?', 'medizco' ),
                        'desc'  => esc_html__('Show or hide the banner', 'medizco'),
                        'value' => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'xs_woo_show_breadcrumb' => [
                        'type'  => 'switch',
                        'label' => esc_html__( 'Show Breadcrumb?', 'medizco' ),
                        'desc'  => esc_html__('Show or hide the Breadcrumb', 'medizco'),
                        'value' => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'xs_woo_banner_title'  => [
                        'type'   => 'text',
                        'label'  => esc_html__( 'Banner Title', 'medizco' ),
                        'value'  => '',
                    ],

                    'xs_woo_banner_image'  =>array(
                        'label'       => esc_html__( 'Banner Image', 'medizco' ),
                        'type'        => 'upload',
                        'images_only' => true,
                        'files_ext'   => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),

                    'xs_woo_banner_bg'=>array(
                        'label'       => esc_html__( 'Banner Background Image', 'medizco' ),
                        'type'        => 'upload',
                        'images_only' => true,
                        'files_ext'   => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    )
                ],
            ],

			'xs_woo_single_banner_setting' => [
                'type'        => 'popup',
                'label'       => esc_html__('Shop Single Banner Settings', 'medizco'),
                'popup-title' => esc_html__('Shop Single Banner Settings', 'medizco'),
                'button'      => esc_html__('Edit Shop Single Banner Button', 'medizco'),
                'size'        => 'medium', // small, medium, large
                'popup-options' => [
                    'xs_woo_single_show_banner' => [
                        'type'  => 'switch',
                        'label' => esc_html__( 'Show Banner?', 'medizco' ),
                        'desc'  => esc_html__('Show or hide the banner', 'medizco'),
                        'value' => 'yes',
                        'left-choice'  => [
                            'value'    => 'yes',
                            'label'    => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice' => [
                            'value'    => 'no',
                            'label'    => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'xs_woo_single_show_breadcrumb' => [
                        'type'  => 'switch',
                        'label' => esc_html__( 'Show Breadcrumb?', 'medizco' ),
                        'desc'  => esc_html__('Show or hide the Breadcrumb', 'medizco'),
                        'value' => 'yes',
                        'left-choice'  => [
                            'value'    => 'yes',
                            'label'    => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice' => [
                            'value'    => 'no',
                            'label'    => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'xs_woo_single_banner_title' => [
                        'type'  => 'text',
                        'label' => esc_html__( 'Banner Title', 'medizco' ),
                        'value' => '',
                    ],

                    'xs_woo_single_banner_image' => array(
                        'label'       => esc_html__( 'Banner Image', 'medizco' ),
                        'type'        => 'upload',
                        'images_only' => true,
                        'files_ext'   => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),

                    'xs_woo_single_banner_bg' => array(
                        'label'       => esc_html__( 'Banner Background Image', 'medizco' ),
                        'type'        => 'upload',
                        'images_only' => true,
                        'files_ext'   => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    )
                ],
            ],

			'xs_woo_shop_page_setting' => [
				'type'         => 'radio',
				'value' => 'fluid',
				'label' => __('Shop Page Layout', 'medizco'),
				'desc'  => __('Select shop page layout style', 'medizco'),
				'choices' => [ // Note: Avoid bool or int keys http://bit.ly/1cQgVzk
					'fluid'   => __('Fluid', '{domain}'),
					'lidebar' => __('Left Sidebar', 'medizco'),
					'rsidbar' => __('Right Sidebar', 'medizco'),
				],
				// Display choices inline instead of list
				'inline' => true,
			],
		],
	],
];