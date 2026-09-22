<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: Header
 */

$header_settings = medizco_option('theme_header_default_settings');
$header_id = '';
$header_builder_enable = medizco_option('header_builder_enable');
if($header_builder_enable=='yes' && isset($header_settings['yes'])){
    $header_id =   $header_settings['yes']['medizco_header_builder_select'];
}

$options =[
    'header_settings' => [
        'title'		 => esc_html__( 'Header settings', 'medizco' ),

        'options'	 => [
            'header_builder_enable' => [
                'type'			   => 'switch',
                'label'			   => esc_html__( 'Header builder Enable', 'medizco' ),
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

            'theme_header_default_settings' => array(
                'type' => 'multi-picker',
                'picker' => 'header_builder_enable',

                'choices' => array(
                    'yes' => array(
                        'medizco_header_builder_select' =>array(
                            'type'  => 'select',

                            'attr'  => array( 'class' => 'xs_header_builder_select', 'data-foo' => 'medizco_header_builder_select' ),
                            'label' => __('Header style', 'medizco'),

                            'choices' => medizco_ekit_headers(),

                            'no-validate' => false,
                        ),
                        'edit_header' => array(
                            'type'  => 'html',
                            'value' => '',

                            'label' => __('edit', 'medizco'),
                            'html'  => '<h2 class="header_builder_edit"><a class="xs_header_builder_edit_link" target="_blank" style="text-transform: uppercase; color:green" href='. admin_url( 'post.php?action=elementor&post='.$header_id ). '>'. esc_html('Edit content here.'). '</a><h2>' ,
                        ),
                    ),



                    'no' => array(

                    )
                )
            ),
        ],
    ]
];
