<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * metabox options for pages
 */

if ( !function_exists('getDoctorDepartments') ):
	function getDoctorDepartments() {
	    $depts = get_terms( 'medizco-departments', 'hide_empty=0' );
	    $arry = array(
	        ''  => __( 'Select A Department', 'medizco' ),
	    );

	    foreach( $depts as $dept ):
	        $arry[ $dept->name ] = $dept->name;
	    endforeach;

	    return $arry;
	}
endif;

$options = array(
	'settings-doctor' => array(
		'title'		 => __( 'Doctor Settings', 'medizco' ),
		'type'		 => 'box',
		'priority'	 => 'high',
		'options'	 => array(
			'doctor_role'	=> array(
				'type'	    	=> 'select',
                'label'	    	=> __( 'Primary Speciality', 'medizco' ),
                'choices'   	=> getDoctorDepartments(),
			),
			'doctor_icon'	=> array(
				'type'	    	=> 'icon-v2',
                'label'	    	=> __( 'Icon', 'medizco' ),
			),
			'doctor_social'	=> array(
				'label'	=> __( 'Social Icons', 'medizco' ),
				'type'  => 'addable-box',
				'box-options' => array(
					'title'		=> array( 'type' => 'text' ),
					'icon'		=> array( 'type' => 'icon' ),
					'color'		=> array( 'type' => 'color-picker' ),
					'link'		=> array( 'type' => 'text' ),
				),
				'template' => '{{- title }}',
			),
        ),
	),
	'settings-page' => array(
		'title'		 => __( 'Page Settings', 'medizco' ),
		'type'		 => 'box',
		'priority'	 => 'high',
		'options'	 => array(
			'header_title'	 => array(
				'type'	 => 'text',
				'label'	 => __( 'Banner Title', 'medizco' ),
				'desc'	 => __( 'Add your Page hero title', 'medizco' ),
			),
			'header_image'	 => array(
				'label'	 => __( 'Banner Image', 'medizco' ),
				'desc'	 => __( 'Upload a page header image', 'medizco' ),
				'type'	 => 'upload'
            ),
			'header_bg_image'	 => array(
				'label'	 => __( 'Banner Background Image', 'medizco' ),
				'desc'	 => __( 'Upload a page header background image', 'medizco' ),
				'type'	 => 'upload'
            ),
        ),
	),
);
