<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: general
 */
$footer_settings = medizco_option('theme_footer_default_settings');
$footer_id = '';
$footer_builder_enable = medizco_option('footer_builder_enable');
if($footer_builder_enable=='yes' && isset($footer_settings['yes'])){
    $footer_id =   $footer_settings['yes']['medizco_footer_builder_select'];
}

$options =[
    'footer_settings' => [
        'title'		 => esc_html__( 'Footer settings', 'medizco' ),

        'options'	 => [
            'footer_builder_enable' => [
                'type'			   => 'switch',
                'label'			   => esc_html__( 'Footer builder Enable', 'medizco' ),
                'desc'			   => '' ,
                'value'           => 'no',
                'left-choice'	 => [
                    'value'	 => 'yes',
                    'label'	 => esc_html__('Yes', 'medizco'),
                ],
                'right-choice'	 => [
                    'value'	 => 'no',
                    'label'	 => esc_html__('No', 'medizco'),
                ],
            ],

            'theme_footer_default_settings' => array(
                'type' => 'multi-picker',
                'picker' => 'footer_builder_enable',

                'choices' => array(
                    'yes' => array(
                        'medizco_footer_builder_select' =>array(
                            'type'  => 'select',

                            'attr'  => array( 'class' => 'xs_header_builder_select', 'data-foo' => 'medizco_header_builder_select' ),
                            'label' => __('Footer style', 'medizco'),

                            'choices' => medizco_ekit_footers(),

                            'no-validate' => false,
                        ),
                        'edit_footer' => array(
                            'type'  => 'html',
                            'value' => '',

                            'label' => __('edit', 'medizco'),
                            'html'  => '<h2 class="header_builder_edit"><a class="xs_header_builder_edit_link" target="_blank" style="text-transform: uppercase; color:green" href='. admin_url( 'post.php?action=elementor&post='.$footer_id ). '>'. esc_html('Edit content here.'). '</a><h2>' ,
                        ),
                    ),



                    'no' => array(

                    )
                )
            ),
            'footer_bg_color' => [
                'label'	 => esc_html__( 'Copyright Background color', 'medizco'),
                'type'	 => 'color-picker',
                'value'  => '',
                'desc'	 => esc_html__( 'You can change the copyright background color with rgba color or solid color', 'medizco'),
            ],
            'footer_copyright_color' => [
                'label'	 => esc_html__( 'Copyright Text color', 'medizco'),
                'type'	 => 'color-picker',
                'desc'	 => esc_html__( 'You can change the footer\'s background color with rgba color or solid color', 'medizco'),
            ],
            'footer_copyright'	 => [
                'type'	 => 'textarea',
                'value'  =>  esc_html__('&copy; '.date('Y').', Medizco. All Rights Reserved.','medizco'),
                'label'	 => esc_html__( 'Copyright text', 'medizco' ),
                'desc'	 => esc_html__( 'This text will be shown at the footer of all pages.', 'medizco' ),
            ],
            'back_to_top'		    => [
                'type'			 => 'switch',
                'value'			 => 'show',
                'label'			 => esc_html__( 'Back To Top Button', 'medizco'),
                'left-choice'	 => [
                    'value'	 => 'show',
                    'label'	 => esc_html__( 'Show', 'medizco'),
                ],
                'right-choice'	 => [
                    'value'	 => 'hide',
                    'label'	 => esc_html__( 'Hide', 'medizco'),
                ],
            ],

        ],

        ]
    ];
