<?php

if ( ! defined( 'ABSPATH' ) ) exit;

class medizco_Shortcode {

	/**
     * Holds the class object.
     *
     * @since 1.0
     *
     */
    public static $_instance;


    /**
     * Localize data array
     *
     * @var array
     */
    public $localize_data = array();

	/**
     * Load Construct
     *
     * @since 1.0
     */

	public function __construct(){
        add_action( 'elementskit/loaded', [$this, 'init'] );
    }


	public function init(){

		add_action( 'elementor/init', array( $this, 'medizco_elementor_init' ) );
        add_action( 'elementor/widgets/widgets_registered', array( $this, 'medizco_shortcode_elements' ) );
        add_action( 'elementor/editor/after_enqueue_styles', array( $this, 'editor_enqueue_styles' ) );
        add_action( 'elementor/frontend/before_enqueue_scripts', array( $this, 'enqueue_scripts' ) );
        add_action( 'elementor/preview/enqueue_styles', array( $this, 'preview_enqueue_scripts' ) );
	}


    /**
     * Enqueue Scripts
     *
     * @return void
     */

    public function enqueue_scripts() {
        wp_enqueue_script( 'mixitup', MEDIZCO_JS  . '/mixitup.min.js', array( 'jquery', 'elementor-frontend' ), MEDIZCO_VERSION, true );
        wp_enqueue_script( 'medizco-main-elementor', MEDIZCO_JS  . '/elementor.js', array( 'jquery', 'elementor-frontend' ), MEDIZCO_VERSION, true );

        // ekit pro script and style
        if (class_exists('ElementsKit_Lite')) {
            if(\ElementsKit_Lite::package_type() == 'free' && !in_array('elementskit/elementskit.php', apply_filters('active_plugins', get_option('active_plugins')))){
                wp_enqueue_style( 'medizco-widget-styles-pro', MEDIZCO_CSS . '/widget-styles-pro.css', null, MEDIZCO_VERSION );
                wp_enqueue_script( 'medizco-widget-scripts-pro', MEDIZCO_JS . '/widget-scripts-pro.js', array( 'jquery', 'elementor-frontend' ), MEDIZCO_VERSION, true );
            }
        }
    }

    /**
     * Enqueue editor styles
     *
     * @return void
     */

    public function editor_enqueue_styles() {
    }

    /**
     * Preview Enqueue Scripts
     *
     * @return void
     */

    public function preview_enqueue_scripts() {}
	/**
     * Elementor Initialization
     *
     * @since 1.0
     *
     */

    public function medizco_elementor_init() {}

    /**
     * Extend Icon pack core controls.
     *
     * @param  object $controls_manager Controls manager instance.
     * @return void
     */

    public function medizco_icon_pack( $controls_manager ) {

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/controls/icon.php';

        $controls = array(
            $controls_manager::ICON => 'MEDIZCO_Icon_Controler',
        );

        foreach ( $controls as $control_id => $class_name ) {
            $controls_manager->unregister_control( $control_id );
            $controls_manager->register_control( $control_id, new $class_name() );
        }

    }

    public function medizco_shortcode_elements( $widgets_manager ){

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/medizco-doctors.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Doctors_Widget() );

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/medizco-doctor-info.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Doctor_Info_Widget() );

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/medizco-doctor-social.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Doctor_Social_Widget() );

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/medizco-services-list.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Services_List_Widget() );

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/medizco-price-list.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Price_List_Widget() );

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/medizco-services-carousel.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Services_Carousel_Widget() );

        require_once MEDIZCO_EDITOR_ELEMENTOR.'/widgets/advanced-tab/advanced-tab.php';
        $widgets_manager->register_widget_type( new Elementor\Medizco_Widget_Advanced_Tab() );

        if ( class_exists( '\Elementor\ElementsKit_Widget_hotspot' ) ) {
            $widgets_manager->register_widget_type(new Elementor\ElementsKit_Widget_hotspot());
        }
        if ( class_exists( '\Elementor\Elementskit_Widget_Chart' ) ) {
            $widgets_manager->register_widget_type(new Elementor\Elementskit_Widget_Chart());
        }
    }

	public static function medizco_get_instance() {
        if (!isset(self::$_instance)) {
            self::$_instance = new medizco_Shortcode();
        }
        return self::$_instance;
    }

}
medizco_Shortcode::medizco_get_instance();


function add_medizco_widget_categories( $elements_manager ) {

	$elements_manager->add_category(
		'medizco-elements',
		[
			'title' => __( 'Medizco', 'medizco' ),
			'icon'  => 'fa fa-plug',
        ]
	);

}
add_action( 'elementor/elements/categories_registered', 'add_medizco_widget_categories' );

if(!defined('ELEMENTOR_PRO_VERSION')){
    add_action( 'elementor/editor/after_enqueue_styles', function() {
        wp_enqueue_style( 'xs-elementor-editor-panel',  MEDIZCO_CSS . '/elementor-editor-panel.css', null,  MEDIZCO_VERSION );
    });
}