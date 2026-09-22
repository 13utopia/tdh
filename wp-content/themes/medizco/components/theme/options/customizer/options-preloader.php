<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: general
 */
$options =[
    'preloader_settings' => [
            'title'		 => esc_html__( 'Preloader settings', 'medizco' ),
            'options'	 => [
                'show_preloader' => array(
                    'type'         => 'multi-picker',
                    'label'        => false,
                    'desc'         => false,
                    'picker'       => array(
                        'show_preloader' => array(
                            'type'			 => 'switch',
                            'label'		 => esc_html__( 'Show Preloader', 'medizco' ),
                            'value'       => 'yes',
                            'left-choice'	 => [
                                'value'   	     => 'yes',
                                'label'	        => esc_html__( 'Yes', 'medizco' ),
                            ],
                            'right-choice'	 => [
                                'value'	 => 'no',
                                'label'	 => esc_html__( 'no', 'medizco' ),
                            ],

                        )
                    ),
                    'choices'      => array(
                        'yes' => array(
                            'preloader_style' => array(
                                'type'         => 'multi-picker',
                                'label'        => false,
                                'desc'         => false,
                                'picker'       => array(
                                    'svg_style' => array(
                                        'type'			 => 'switch',
                                        'label'		 => esc_html__( 'Custom SVG', 'medizco' ),
                                        'value'       => 'custom',
                                        'left-choice'	 => [
                                            'value'   	     => 'custom',
                                            'label'	        => esc_html__( 'Custom', 'medizco' ),
                                        ],
                                        'right-choice'	 => [
                                            'value'	 => 'simple',
                                            'label'	 => esc_html__( 'Simple', 'medizco' ),
                                        ],

                                    )
                                ),
                                'choices'      => array(
                                    'custom' => array(
                                        'custom_svg'=> array(
                                            'type'  => 'textarea',
                                            'value' => '<svg width="45" height="45" viewBox="0 0 45 45" xmlns="http://www.w3.org/2000/svg" stroke="#A6A6A6">
                                            <g fill="none" fill-rule="evenodd" transform="translate(1 1)" stroke-width="2">
                                                <circle cx="22" cy="22" r="6" stroke-opacity="0">
                                                    <animate attributeName="r"
                                                         begin="1.5s" dur="3s"
                                                         values="6;22"
                                                         calcMode="linear"
                                                         repeatCount="indefinite" />
                                                    <animate attributeName="stroke-opacity"
                                                         begin="1.5s" dur="3s"
                                                         values="1;0" calcMode="linear"
                                                         repeatCount="indefinite" />
                                                    <animate attributeName="stroke-width"
                                                         begin="1.5s" dur="3s"
                                                         values="2;0" calcMode="linear"
                                                         repeatCount="indefinite" />
                                                </circle>
                                                <circle cx="22" cy="22" r="6" stroke-opacity="0">
                                                    <animate attributeName="r"
                                                         begin="3s" dur="3s"
                                                         values="6;22"
                                                         calcMode="linear"
                                                         repeatCount="indefinite" />
                                                    <animate attributeName="stroke-opacity"
                                                         begin="3s" dur="3s"
                                                         values="1;0" calcMode="linear"
                                                         repeatCount="indefinite" />
                                                    <animate attributeName="stroke-width"
                                                         begin="3s" dur="3s"
                                                         values="2;0" calcMode="linear"
                                                         repeatCount="indefinite" />
                                                </circle>
                                                <circle cx="22" cy="22" r="8">
                                                    <animate attributeName="r"
                                                         begin="0s" dur="1.5s"
                                                         values="6;1;2;3;4;5;6"
                                                         calcMode="linear"
                                                         repeatCount="indefinite" />
                                                </circle>
                                            </g>
                                        </svg>',
                                            'label' => __('Custom SVG Code', 'medizco'),
                                            'desc'  => '<a href="'. esc_url( 'https://support.xpeedstudio.com/knowledgebase/how-to-create-your-own-svg-preloader-with-animation-for-medizco-theme/' ) .'" target="_blank">'.__('Please check how to create your own svg preloader with animation', 'medizco').'</a>',

                                        )
                                    ),
                                    'simple' => array(
                                        'preloader'=> array(
                                            'type'  => 'image-picker',
                                            'value' => 'oval',
                                            'label' => false,
                                            'choices' => array(
                                                'oval' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/oval.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'audio' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/audio.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'ball-triangle' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/ball-triangle.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'bars' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/bars.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'circles' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/circles.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'grid' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/grid.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'hearts' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/hearts.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'puff' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/puff.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'rings' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/rings.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),'spinning-circles' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/spinning-circles.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                                'three-dots' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/three-dots.svg',
                                                        'height' => 45,
                                                        'width' => 45,

                                                    ),
                                                ),
                                                'tail-spin' => array(
                                                    // (required) url for thumbnail
                                                    'small' => array(
                                                        'src' => MEDIZCO_IMG.'/preloader/tail-spin.svg',
                                                        'height' => 45,
                                                        'width' => 45,
                                                    ),
                                                ),
                                            ),
                                            /**
                                             * Allow save not existing choices
                                             * Useful when you use the select to populate it dynamically from js
                                             */
                                            'no-validate' => false,
                                        )
                                    ),



                                ),
                                'show_borders' => false,
                            ),
                        ),



                    ),
                    'show_borders' => false,
                ),



            ],
        ],
    ];