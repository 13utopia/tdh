<?php if (!defined('ABSPATH')) die('Direct access forbidden.');

$options = array(
    'license' => array(
        'type'  => 'html',
        'value' => 'default hidden value',
        'attr'  => array( 'class' => 'custom-class', 'data-foo' => 'bar' ),
        'label' => __('Activate the theme license', 'medizco'),
        'help'  => __('Goto Admin Dashboard => Appearance => License and active your license', 'medizco'),
        'html'  => 'In order to get regular update, support and demo content, you must activate the theme license. Please <a href="'. admin_url('themes.php?page=license') .'">Goto License Page</a> and activate the theme license as soon as possible.',
    ),
);

