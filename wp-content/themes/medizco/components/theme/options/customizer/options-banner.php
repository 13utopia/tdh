<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: banner
 */


$options = [
    'banner_setting' => [
        'title' => esc_html__('Banner settings', 'medizco'),

        'options' => [
            'page_banner_setting' => [
                'type'        => 'popup',
                'label'       => esc_html__('Page Banner Settings', 'medizco'),
                'popup-title' => esc_html__('Page Banner Settings', 'medizco'),
                'button'      => esc_html__('Edit Page Banner Button', 'medizco'),
                'size'        => 'medium', // small, medium, large
                'popup-options' => [
                    'page_show_banner' => [
                        'type'			 => 'switch',
                        'label'			 => esc_html__( 'Show Banner?', 'medizco' ),
                        'desc'          => esc_html__('Show or hide the banner', 'medizco'),
                        'value'         => 'yes',
                        'left-choice'	 => [
                            'value'	 => 'yes',
                            'label'	 => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'	 => [
                            'value'	 => 'no',
                            'label'	 => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'page_show_breadcrumb' => [
                        'type'			 => 'switch',
                        'label'			 => esc_html__( 'Show Breadcrumb?', 'medizco' ),
                        'desc'          => esc_html__('Show or hide the Breadcrumb', 'medizco'),
                        'value'         => 'yes',
                        'left-choice'	 => [
                            'value'	 => 'yes',
                            'label'	 => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'	 => [
                            'value'	 => 'no',
                            'label'	 => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'banner_bottom_bg_overlay_color' => array(
                        'type'  => 'rgba-color-picker',
                        'value' => 'rgba(28, 186, 159, 0.68)',
                        'label' => __('Breadcumb Banner Overlay Color', 'medizco'),
                    ),
                    'banner_breadcumb_title_color' => array(
                        'type'  => 'color-picker',
                        'value' => '#1cba9f',
                        'label' => __('Breadcumb Title Color', 'medizco'),
                    ),
                    'banner_page_title'	 => [
                        'type'	 => 'text',
                        'label'	 => esc_html__( 'Banner Title', 'medizco' ),
                        'value'  => '',
                    ],
                    'banner_page_image'	 =>array(
                        'label'			 => esc_html__( 'Banner Image', 'medizco' ),
                        'type'			 => 'upload',
                        'images_only'	 => true,
                        'files_ext'		 => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),

                    'banner_page_bg'	 =>array(
                        'label'			 => esc_html__( 'Banner Background Image', 'medizco' ),
                        'type'			 => 'upload',
                        'images_only'	 => true,
                        'files_ext'		 => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),
                ],
            ],
            'blog_banner_setting' => [
                'type'        => 'popup',
                'label'       => esc_html__('Blog Banner Settings', 'medizco'),
                'popup-title' => esc_html__('Blog Banner Settings', 'medizco'),
                'button'      => esc_html__('Edit Blog Banner Button', 'medizco'),
                'size'        => 'medium', // small, medium, large
                'popup-options' => [
                    'blog_show_banner' => [
                        'type'           => 'switch',
                        'label'          => esc_html__( 'Show Banner?', 'medizco' ),
                        'desc'           => esc_html__('Show or hide the banner', 'medizco'),
                        'value'          => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'blog_show_breadcrumb' => [
                        'type'           => 'switch',
                        'label'          => esc_html__( 'Show Breadcrumb?', 'medizco' ),
                        'desc'           => esc_html__('Show or hide the Breadcrumb', 'medizco'),
                        'value'          => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'banner_bottom_bg_overlay_color' => array(
                        'type'  => 'rgba-color-picker',
                        'value' => 'rgba(28, 186, 159, 0.68)',
                        'label' => __('Breadcumb Banner Overlay Color', 'medizco'),
                    ),
                    'banner_breadcumb_title_color' => array(
                        'type'  => 'color-picker',
                        'value' => '#1cba9f',
                        'label' => __('Breadcumb Title Color', 'medizco'),
                    ),
                    'blog_banner_title'  => [
                        'type'   => 'text',
                        'label'  => esc_html__( 'Banner Title', 'medizco' ),
                        'value'  => '',
                    ],

                    'blog_banner_image'  =>array(
                        'label'          => esc_html__( 'Banner Image', 'medizco' ),
                        'type'           => 'upload',
                        'images_only'    => true,
                        'files_ext'      => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),

                    'blog_banner_bg'     =>array(
                        'label'          => esc_html__( 'Banner Background Image', 'medizco' ),
                        'type'           => 'upload',
                        'images_only'    => true,
                        'files_ext'      => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    )
                ],
            ],
            'blog_category_banner_setting' => [
                'type'        => 'popup',
                'label'       => esc_html__('Blog Category Banner Settings', 'medizco'),
                'popup-title' => esc_html__('Category Banner Settings', 'medizco'),
                'button'      => esc_html__('Edit Category Banner', 'medizco'),
                'size'        => 'medium', // small, medium, large
                'popup-options' => [
                    'blog_category_show_banner' => [
                        'type'           => 'switch',
                        'label'          => esc_html__( 'Show Banner?', 'medizco' ),
                        'desc'           => esc_html__('Show or hide the banner', 'medizco'),
                        'value'          => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'blog_category_show_breadcrumb' => [
                        'type'           => 'switch',
                        'label'          => esc_html__( 'Show Breadcrumb?', 'medizco' ),
                        'desc'           => esc_html__('Show or hide the Breadcrumb', 'medizco'),
                        'value'          => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'banner_bottom_bg_overlay_color' => array(
                        'type'  => 'rgba-color-picker',
                        'value' => 'rgba(28, 186, 159, 0.68)',
                        'label' => __('Breadcumb Banner Overlay Color', 'medizco'),
                    ),
                    'banner_breadcumb_title_color' => array(
                        'type'  => 'color-picker',
                        'value' => '#1cba9f',
                        'label' => __('Breadcumb Title Color', 'medizco'),
                    ),
                    'blog_category_banner_title'  => [
                        'type'   => 'text',
                        'label'  => esc_html__( 'Banner Title', 'medizco' ),
                        'value'  => '',
                    ],

                    'blog_category_banner_image'  =>array(
                        'label'          => esc_html__( 'Banner Image', 'medizco' ),
                        'type'           => 'upload',
                        'images_only'    => true,
                        'files_ext'      => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),

                    'blog_category_banner_bg'     =>array(
                        'label'          => esc_html__( 'Banner Background Image', 'medizco' ),
                        'type'           => 'upload',
                        'images_only'    => true,
                        'files_ext'      => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),
                ],
            ],
            'service_banner_setting' => [
                'type'        => 'popup',
                'label'       => esc_html__('Service Single Banner Settings', 'medizco'),
                'popup-title' => esc_html__('Service Single Banner Settings', 'medizco'),
                'button'      => esc_html__('Edit Service Single Banner', 'medizco'),
                'size'        => 'medium', // small, medium, large
                'popup-options' => [
                    'service_show_banner' => [
                        'type'           => 'switch',
                        'label'          => esc_html__( 'Show Banner?', 'medizco' ),
                        'desc'           => esc_html__('Show or hide the banner', 'medizco'),
                        'value'          => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'service_show_breadcrumb' => [
                        'type'           => 'switch',
                        'label'          => esc_html__( 'Show Breadcrumb?', 'medizco' ),
                        'desc'           => esc_html__('Show or hide the Breadcrumb', 'medizco'),
                        'value'          => 'yes',
                        'left-choice'    => [
                            'value'  => 'yes',
                            'label'  => esc_html__( 'Yes', 'medizco' ),
                        ],
                        'right-choice'   => [
                            'value'  => 'no',
                            'label'  => esc_html__( 'No', 'medizco' ),
                        ],
                    ],
                    'banner_bottom_bg_overlay_color' => array(
                        'type'  => 'rgba-color-picker',
                        'value' => 'rgba(28, 186, 159, 0.68)',
                        'label' => __('Breadcumb Banner Overlay Color', 'medizco'),
                    ),
                    'banner_breadcumb_title_color' => array(
                        'type'  => 'color-picker',
                        'value' => '#1cba9f',
                        'label' => __('Breadcumb Title Color', 'medizco'),
                    ),
                    'service_banner_title'  => [
                        'type'   => 'text',
                        'label'  => esc_html__( 'Banner Title', 'medizco' ),
                        'value'  => '',
                    ],

                    'service_banner_image'  =>array(
                        'label'          => esc_html__( 'Banner Image', 'medizco' ),
                        'type'           => 'upload',
                        'images_only'    => true,
                        'files_ext'      => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),

                    'service_banner_bg'     =>array(
                        'label'          => esc_html__( 'Banner Background Image', 'medizco' ),
                        'type'           => 'upload',
                        'images_only'    => true,
                        'files_ext'      => array( 'jpg', 'png', 'jpeg', 'gif', 'svg' ),
                    ),
                ],
            ],
        ],
    ],
];
