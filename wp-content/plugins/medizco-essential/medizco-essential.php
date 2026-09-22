<?php
/*
* Plugin Name: Medizco Essentials
* License - GNU/GPL V2 or Later
* Description: This is a required plugin for Medizco theme.
* Version: 1.6
* text domain: medizco-essential
*/
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Add language
add_action( 'init', 'medizco_language_load' );
function medizco_language_load(){
    $plugin_dir = basename(dirname(__FILE__))."/languages/";
    load_plugin_textdomain( 'medizco-essential', false, $plugin_dir );
}

// Main Class
class Medizco_Essentials_Includes {

    // Auto load
    // ----------------------------------------------------------------------------------------
	public static function init() {
        self::_action_init();
        add_action( 'widgets_init', array( __CLASS__, '_action_widgets_init' ) );
	}


    // Directory name to class name, transform dynamically
    // ----------------------------------------------------------------------------------------
	private static function dirname_to_classname( $dirname ) {
		$class_name	 = explode( '-', $dirname );
		$class_name	 = array_map( 'ucfirst', $class_name );
		$class_name	 = implode( '_', $class_name );

		return $class_name;
    }

    // Include and register widgets
    // ----------------------------------------------------------------------------------------
	public static function include_widget( $widget_dir ) {
        $rel_path = '/widgets';
        $path = self::get_path( $rel_path ) . '/' . $widget_dir;
        if ( file_exists( $path ) ) {
            self::include_isolated( $path . '/widget-class.php' );
        }

		register_widget( 'Medizco_' . self::dirname_to_classname( $widget_dir ) );
	}

    // include method
    // ----------------------------------------------------------------------------------------
	public static function include_isolated( $path ) {
        include $path;
	}

    // directory path for theme core
    // ----------------------------------------------------------------------------------------
	private static function get_path( $append = '' ) {
		$path = plugin_dir_path( __FILE__ ) . 'includes';
		return $path . $append;
    }

    // include widgets
    // ----------------------------------------------------------------------------------------
	public static function _action_widgets_init() {
        self::include_widget('footer-address');
    }

    // include files
    // ----------------------------------------------------------------------------------------
	public static function _action_init() {
        self::include_isolated( self::get_path('/post-type/post-class.php') );
        self::include_isolated( self::get_path('/helper.php') );
    }
}

Medizco_Essentials_Includes::init();

include 'modules/init.php';
