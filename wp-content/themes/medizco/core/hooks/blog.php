<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * hooks for wp blog part
 */

// if there is no excerpt, sets a defult placeholder
// ----------------------------------------------------------------------------------------
function medizco_excerpt( $words = 20, $more = 'BUTTON' ) {
	if($more == 'BUTTON'){
		$more = '<a class="btn btn-primary">'.esc_html__('read more', 'medizco').'</a>';
	}
	$excerpt		 = get_the_excerpt();
	$trimmed_content = wp_trim_words( $excerpt, $words, $more );
	echo medizco_kses( $trimmed_content );
}


// change textarea position in comment form
// ----------------------------------------------------------------------------------------
function medizco_move_comment_textarea_to_bottom( $fields ) {
	$comment_field		 = $fields[ 'comment' ];
	unset( $fields[ 'comment' ] );
	$fields[ 'comment' ] = $comment_field;
	return $fields;
}
add_filter( 'comment_form_fields', 'medizco_move_comment_textarea_to_bottom' );


// change textarea position in comment form
// ----------------------------------------------------------------------------------------
function medizco_search_form( $form ) {
    $form = '
        <form  method="get" action="' . esc_url( home_url( '/' ) ) . '" class="medizco-serach xs-search-group">
            <div class="input-group">
                <input type="search" class="form-control" name="s" placeholder="' .esc_attr__( 'Search', 'medizco' ) . '" value="' . get_search_query() . '">
                <button class="input-group-btn search-button"><i class="fa fa-search"></i></button>
            </div>
        </form>';
	return $form;
}
add_filter( 'get_search_form', 'medizco_search_form' );

function medizco_body_classes( $classes ) {
    $blogSidebar = medizco_option( 'blog_sidebar' );
    $sidebar1 = is_active_sidebar( 'sidebar-1' );

    if ( $sidebar1 ):
        $classes[] = $blogSidebar != 1 ? 'sidebar-active' : 'sidebar-inactive';
    else:
        $classes[] = 'sidebar-inactive';
    endif;

    $box_class =  medizco_option('general_body_box_layout');

    if(isset($box_class['style'])){
        if($box_class['style']=='yes'){
         $classes[] = 'body-box-layout';
        }
    }
 
    return $classes;
 }
 
 add_filter( 'body_class','medizco_body_classes' );


