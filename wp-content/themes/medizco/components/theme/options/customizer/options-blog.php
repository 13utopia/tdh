<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * customizer option: blog
 */

$options =[
    'blog_settings' => [
        'title'		 => esc_html__( 'Blog settings', 'medizco' ),

        'options'	 => [
            'blog_sidebar' =>[
                'type'  => 'select',
                              
                'label' => esc_html__('Sidebar', 'medizco'),
                'desc'  => esc_html__('Description', 'medizco'),
                'help'  => esc_html__('Help tip', 'medizco'),
                'choices' => array(
                    '1' => esc_html__('No sidebar','medizco'),
                    '2' => esc_html__('Left Sidebar', 'medizco'),
                    '3' => esc_html__('Right Sidebar', 'medizco'),
                 
                 ),
              
                'no-validate' => false,
            ],   

            'blog_author' => [
                'type'			 => 'switch',
                'label'			 => esc_html__( 'Blog author', 'medizco' ),
                'desc'			 => esc_html__( 'Do you want to show blog author?', 'medizco' ),
                'value'          => 'no',
                'left-choice' => [
                    'value'	 => 'yes',
                    'label'	 => esc_html__( 'Yes', 'medizco' ),
                ],
                'right-choice' => [
                    'value'	 => 'no',
                    'label'	 => esc_html__( 'No', 'medizco' ),
                ],
           ],
        ],
            
        ]
    ];