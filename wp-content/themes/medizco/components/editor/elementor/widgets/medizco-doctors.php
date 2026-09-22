<?php

namespace Elementor;
// use \ElementsKit_Lite\Modules\Controls\Controls_Manager as ElementsKit_Controls_Manager;

if ( ! defined( 'ABSPATH' ) ) exit;

class Medizco_Doctors_Widget extends Widget_Base {

    public function __construct( $data = [], $args = null ) {
        parent::__construct( $data, $args );
        $this->add_script_depends('slick');
    }

    public function get_name() {
        return 'medizco-doctors';
    }

    public function get_title() {
        return esc_html__( 'Medizco Doctors', 'medizco' );
    }

    public function get_icon() {
        return 'fa fa-user-md';
    }

    public function get_categories() {
        return ['medizco-elements'];
    }

    protected function register_controls() {

        $this->start_controls_section('section_tab_style',
            [
                'label' => esc_html__( 'Medizco Doctors', 'medizco' ),
            ]
        );

        $this->add_control(
            'medizco_doctors_style',
            [
                'label'     => esc_html__( 'Choose Style', 'medizco' ),
                'type'      => 'imagechoose',
                'default'   => 'medizco_doctors_slider',
                'options'   => [
                    'medizco_doctors_slider' => [
                        'title'         => esc_html__( 'Slider', 'medizco' ),
                        'imagelarge'    => MEDIZCO_IMG . '/doctors-style/slider.jpg',
                        'imagesmall'    => MEDIZCO_IMG . '/doctors-style/slider.jpg',
                        'width'         => '50%',
                    ],
                    'medizco_doctors_filter' => [
                        'title'         => esc_html__( 'Filter', 'medizco' ),
                        'imagelarge'    => MEDIZCO_IMG . '/doctors-style/filter.jpg',
                        'imagesmall'    => MEDIZCO_IMG . '/doctors-style/filter.jpg',
                        'width'         => '50%',
                    ],
                ],
            ]
        );
        $this->add_control(
            'medizco_doctors_count',
            [
                'label'         => esc_html__( 'Post Count', 'medizco' ),
                'type'          => Controls_Manager::NUMBER,
                'default'       => esc_html__( '12', 'medizco' ),
            ]
        );
        $this->add_control(
            'medizco_doctors_dept',
            [
                'label'     => esc_html__( 'Departments', 'medizco' ),
                'type'      => \Elementor\Controls_Manager::SELECT2,
                'multiple'  => true,
                'default'   => '',
                'options'   => $this->getCategories('medizco-departments'),
                'condition' => [
                    'medizco_doctors_style' => 'medizco_doctors_slider'
                ],
            ]
        );
        $this->add_control(
            'medizco_team_offset',
            [
                'label'     => esc_html__( 'Offset', 'medizco' ),
                'type'      => Controls_Manager::NUMBER,
                'min'       => 0,
                'max'       => 20,
                'default'   => 0,
            ]
        );

        $this->add_control(
            'medizco_team_order_by',
            [
                'label'   => esc_html__( 'Order by', 'medizco' ),
                'type'    => Controls_Manager::SELECT,
                'options' => [
                    'date'          => esc_html__( 'Date', 'medizco' ),
                    'title'         => esc_html__( 'Title', 'medizco' ),
                    'author'        => esc_html__( 'Author', 'medizco' ),
                    'modified'      => esc_html__( 'Modified', 'medizco' ),
                    'comment_count' => esc_html__( 'Comments', 'medizco' ),
                ],
                'default' => 'date',
            ]
        );

        $this->add_control(
            'medizco_team_sort',
            [
                'label'   => esc_html__( 'Order', 'medizco' ),
                'type'    => Controls_Manager::SELECT,
                'options' => [
                    'ASC'  => esc_html__( 'ASC', 'medizco' ),
                    'DESC' => esc_html__( 'DESC', 'medizco' ),
                ],
                'default' => 'DESC',
            ]
        );
        $this->end_controls_section();

        // Style Tab Controls
        $this->start_controls_section('filter_style_section',
            [
                'label'     => esc_html__( 'Filter Nav', 'medizco' ),
                'tab'       => Controls_Manager::TAB_STYLE,
                'condition' => [
                    'medizco_doctors_style' => 'medizco_doctors_filter'
                ],
            ]
        );
            $this->add_control(
                'medizco_doctors_filter_color',
                [
                    'label'     => __( 'Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#1cba9f',
                    'selectors' => [
                        '{{WRAPPER}} .filter_nav > li' => 'border-color: {{VALUE}}',
                        '{{WRAPPER}} .filter_nav > li:hover' => 'color: {{VALUE}}',
                        '{{WRAPPER}} .filter_nav > li.active' => 'color: {{VALUE}}',
                        '{{WRAPPER}} .filter_nav > li.mixitup-control-active' => 'color: {{VALUE}}',
                    ],
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section('style_section',
            [
                'label'    => esc_html__( 'Doctor Box', 'medizco' ),
                'tab'      => Controls_Manager::TAB_STYLE,
            ]
        );
            $this->add_control(
                'medizco_doctor_box_align',
                [
                    'label'     => esc_html__( 'Alignment', 'medizco' ),
                    'type'      => Controls_Manager::CHOOSE,
                    'options'   => [
                        'left'      => [
                            'title'     => esc_html__( 'Left', 'medizco' ),
                            'icon'      => 'fa fa-align-left',
                        ],
                        'center'    => [
                            'title'     => esc_html__( 'Center', 'medizco' ),
                            'icon'      => 'fa fa-align-center',
                        ],
                        'right'     => [
                            'title'     => esc_html__( 'Right', 'medizco' ),
                            'icon'      => 'fa fa-align-right',
                        ],
                    ],
                    'selectors' => [
                        '{{WRAPPER}} .doctor_box' => 'text-align: {{VALUE}};'
                    ],
                    'default'   => 'center',
                ]
            );
            $this->start_controls_tabs( 'medizco_doctor_box_tabs' );
                $this->start_controls_tab(
                    'medizco_doctor_box_tab_n',
                    [
                        'label' => esc_html__( 'Normal', 'medizco' ),
                    ]
                );
                    $this->add_control(
                        'medizco_doctor_box_n_bg',
                        [
                            'label'     => __( 'Background Color', 'medizco' ),
                            'type'      => \Elementor\Controls_Manager::COLOR,
                            'default'   => '#fff',
                            'selectors' => [
                                '{{WRAPPER}} .doctor_box' => 'background-color: {{VALUE}}',
                            ],
                        ]
                    );
                    $this->add_group_control(
                        Group_Control_Box_Shadow::get_type(),
                        [
                            'name'      => 'medizco_doctor_box_n_shadow',
                            'label'     => __( 'Box Shadow', 'medizco' ),
                            'selector'  => '{{WRAPPER}} .doctor_box',
                        ]
                    );
                $this->end_controls_tab();
                $this->start_controls_tab(
                    'medizco_doctor_box_tab_h',
                    [
                        'label' => esc_html__( 'Hover', 'medizco' ),
                    ]
                );
                    $this->add_control(
                        'medizco_doctor_box_h_bg',
                        [
                            'label'     => __( 'Background Color', 'medizco' ),
                            'type'      => \Elementor\Controls_Manager::COLOR,
                            'default'   => '',
                            'selectors' => [
                                '{{WRAPPER}} .doctor_box:hover' => 'background-color: {{VALUE}}',
                            ],
                        ]
                    );
                    $this->add_group_control(
                        Group_Control_Box_Shadow::get_type(),
                        [
                            'name'      => 'medizco_doctor_box_h_shadow',
                            'label'     => __( 'Box Shadow', 'medizco' ),
                            'selector'  => '{{WRAPPER}} .doctor_box:hover',
                        ]
                    );
                $this->end_controls_tab();
            $this->end_controls_tabs();
        $this->end_controls_section();

        $this->start_controls_section('medizco_doctors_img_section',
            [
                'label'    => esc_html__( 'Image', 'medizco' ),
                'tab'      => Controls_Manager::TAB_STYLE,
            ]
        );
            $this->add_control(
                'medizco_doctor_box_overlay',
                [
                    'label'     => __( 'Overlay', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#1cba9f',
                    'selectors' => [
                        '{{WRAPPER}} .doctor_box_social:before' => 'background-image: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, {{VALUE}} 100%);',
                    ],
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section('medizco_doctors_social_section',
            [
                'label'    => esc_html__( 'Social Icons', 'medizco' ),
                'tab'      => Controls_Manager::TAB_STYLE,
            ]
        );
            $this->add_control(
                'medizco_doctor_box_icons_color',
                [
                    'label'     => __( 'Primary Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#1cba9f',
                    'selectors' => [
                        '{{WRAPPER}} .doctor_box_social i' => 'color: {{VALUE}}',
                        '{{WRAPPER}} .doctor_box_social span' => 'background-color: {{VALUE}}',
                    ],
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section('medizco_doctors_content_section',
            [
                'label'    => esc_html__( 'Contents', 'medizco' ),
                'tab'      => Controls_Manager::TAB_STYLE,
            ]
        );
            $this->add_group_control(
                Group_Control_Border::get_type(),
                [
                    'name'      => 'medizco_doctor_box_content_bd',
                    'label'     => __( 'Border', 'medizco' ),
                    'selector'  => '{{WRAPPER}} .doctor_box_content',
                ]
            );
            $this->add_control(
                'medizco_doctor_box_content_padding',
                [
                    'label'         => __( 'Padding', 'medizco' ),
                    'type'          => Controls_Manager::DIMENSIONS,
                    'size_units'    => [ 'px' ],
                    'selectors'     => [
                        '{{WRAPPER}} .doctor_box_content' => 'padding: {{TOP}}{{UNIT}} {{RIGHT}}{{UNIT}} {{BOTTOM}}{{UNIT}} {{LEFT}}{{UNIT}};',
                    ],
                    'default'       => [
                        'top'           => 41,
                        'left'          => 0,
                        'right'         => 0,
                        'bottom'        => 32,
                    ]
                ]
            );

            $this->add_control(
                'medizco_doctor_box_icon_h',
                [
                    'label'     => __( 'Icon', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::HEADING,
                    'separator' => 'before',
                ]
            );
            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'medizco_doctor_box_icon_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .doctor_box_icon > .doctor_box_icon_item',
                    'fields_options'    => [
                        'font_size' => [
                            'default'   => [
                                'unit'  => 'px',
                                'size'  => 18
                            ]
                        ],
                        'line_height' => [
                            'default'   => [
                                'unit'  => 'px',
                                'size'  => 38
                            ]
                        ],
                    ],
                ]
            );
            $this->start_controls_tabs( 'medizco_doctor_box_icon_tabs' );
                $this->start_controls_tab(
                    'medizco_doctor_box_icon_tab_n',
                    [
                        'label' => esc_html__( 'Normal', 'medizco' ),
                    ]
                );
                    $this->add_control(
                        'medizco_doctor_box_icon_n_c',
                        [
                            'label'     => __( 'Color', 'medizco' ),
                            'type'      => \Elementor\Controls_Manager::COLOR,
                            'default'   => '#fff',
                            'selectors' => [
                                '{{WRAPPER}} .doctor_box_icon > .doctor_box_icon_item' => 'color: {{VALUE}}',
                            ],
                        ]
                    );
                    $this->add_control(
                        'medizco_doctor_box_icon_n_bgc',
                        [
                            'label'     => __( 'Background-Color', 'medizco' ),
                            'type'      => \Elementor\Controls_Manager::COLOR,
                            'default'   => '#1cba9f',
                            'selectors' => [
                                '{{WRAPPER}} .doctor_box_icon > .doctor_box_icon_item' => 'background-color: {{VALUE}}',
                            ],
                        ]
                    );

                    $this->add_group_control(
                        Group_Control_Border::get_type(),
                        [
                            'name'      => 'medizco_doctor_box_icon_n_bd',
                            'label'     => __( 'Border', 'medizco' ),
                            'selector'  => '{{WRAPPER}} .doctor_box_icon > .doctor_box_icon_item',
                            'fields_options'    => [
                                'border' => [
                                    'default'   => 'solid',
                                ],
                                'width' => [
                                    'default'   => array(
                                        'top'       => 1,
                                        'left'      => 1,
                                        'right'     => 1,
                                        'bottom'    => 1,
                                    ),
                                    'responsive'    => false,
                                ],
                                'color' => [
                                    'default'   => '#1cba9f',
                                ],
                            ],
                        ]
                    );
                $this->end_controls_tab();
                $this->start_controls_tab(
                    'medizco_doctor_box_icon_tab_h',
                    [
                        'label' => esc_html__( 'Normal', 'medizco' ),
                    ]
                );
                    $this->add_control(
                        'medizco_doctor_box_icon_h_c',
                        [
                            'label'     => __( 'Color', 'medizco' ),
                            'type'      => \Elementor\Controls_Manager::COLOR,
                            'default'   => '#1cba9f',
                            'selectors' => [
                                '{{WRAPPER}} .doctor_box:hover .doctor_box_icon > .doctor_box_icon_item' => 'color: {{VALUE}}',
                            ],
                        ]
                    );
                    $this->add_control(
                        'medizco_doctor_box_icon_h_bgc',
                        [
                            'label'     => __( 'Background-Color', 'medizco' ),
                            'type'      => \Elementor\Controls_Manager::COLOR,
                            'default'   => '#fff',
                            'selectors' => [
                                '{{WRAPPER}} .doctor_box:hover .doctor_box_icon > .doctor_box_icon_item' => 'background-color: {{VALUE}}',
                            ],
                        ]
                    );

                    $this->add_group_control(
                        Group_Control_Border::get_type(),
                        [
                            'name'      => 'medizco_doctor_box_icon_h_bd',
                            'label'     => __( 'Border', 'medizco' ),
                            'selector'  => '{{WRAPPER}} .doctor_box:hover .doctor_box_icon > .doctor_box_icon_item',
                        ]
                    );
                $this->end_controls_tab();
            $this->end_controls_tabs();

            $this->add_control(
                'medizco_doctor_box_title_h',
                [
                    'label'     => __( 'Title', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::HEADING,
                    'separator' => 'before',
                ]
            );
            $this->add_control(
                'medizco_doctor_box_title_color',
                [
                    'label'     => __( 'Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#222',
                    'selectors' => [
                        '{{WRAPPER}} .doctor_box_title' => 'color: {{VALUE}}',
                    ],
                ]
            );
            $this->add_control(
                'medizco_doctor_box_title_hcolor',
                [
                    'label'     => __( 'Hover Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#1cba9f',
                    'selectors' => [
                        '{{WRAPPER}} .doctor_box:hover .doctor_box_title' => 'color: {{VALUE}}',
                    ],
                ]
            );
            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'medizco_doctor_box_title_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .doctor_box_title',
                    'fields_options'    => [
                        'font_size' => [
                            'default'   => [
                                'unit'  => 'px',
                                'size'  => 20
                            ]
                        ],
                    ],
                ]
            );
            $this->add_control(
                'medizco_doctor_box_title_margin',
                [
                    'label'         => __( 'Margin', 'medizco' ),
                    'type'          => Controls_Manager::DIMENSIONS,
                    'size_units'    => [ 'px' ],
                    'selectors'     => [
                        '{{WRAPPER}} .doctor_box_title' => 'margin: {{TOP}}{{UNIT}} {{RIGHT}}{{UNIT}} {{BOTTOM}}{{UNIT}} {{LEFT}}{{UNIT}};',
                    ],
                    'default'       => [
                        'top'           => 0,
                        'left'          => 0,
                        'right'         => 0,
                        'bottom'        => 0,
                    ],
                ]
            );

            $this->add_control(
                'medizco_doctor_box_role_h',
                [
                    'label'     => __( 'Designation', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::HEADING,
                    'separator' => 'before',
                ]
            );
            $this->add_control(
                'medizco_doctor_box_role_color',
                [
                    'label'     => __( 'Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#222',
                    'selectors' => [
                        '{{WRAPPER}} .doctor_box_role' => 'color: {{VALUE}}',
                    ],
                ]
            );
            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'medizco_doctor_box_role_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .doctor_box_role',
                    'fields_options'    => [
                        'font_size' => [
                            'default'   => [
                                'unit'  => 'px',
                                'size'  => 13
                            ]
                        ],
                    ],
                ]
            );
            $this->add_control(
                'medizco_doctor_box_role_margin',
                [
                    'label'         => __( 'Margin', 'medizco' ),
                    'type'          => Controls_Manager::DIMENSIONS,
                    'size_units'    => [ 'px' ],
                    'selectors'     => [
                        '{{WRAPPER}} .doctor_box_role' => 'margin: {{TOP}}{{UNIT}} {{RIGHT}}{{UNIT}} {{BOTTOM}}{{UNIT}} {{LEFT}}{{UNIT}};',
                    ]
                ]
            );
        $this->end_controls_section();

    }

    protected function render( ) {
        $settings = $this->get_settings();
        $settings_val = $this->get_settings_for_display();

        extract( $settings );

        $paged = 1;
        if ( get_query_var('paged') ) $paged = get_query_var('paged');
        if ( get_query_var('page') ) $paged = get_query_var('page');

        $query = array(
            'post_type'     => 'medizco-doctor',
            'post_status'   => 'publish',
            'posts_per_page'=> $medizco_doctors_count,
            'paged'         => $paged
        );

        if ( 'medizco_doctors_slider' == $medizco_doctors_style && !empty( $medizco_doctors_dept ) ):
            $query['tax_query'] = array(
                array(
                    'taxonomy'  => 'medizco-departments',
                    'terms'     => $medizco_doctors_dept,
                    'field'     => 'id',
                )
            );
        endif;

        if ($medizco_team_order_by != '') {
            $query['orderby'] = $medizco_team_order_by;
        }

        if ($medizco_team_sort != '') {
            $query['order'] = $medizco_team_sort;
        }

        if ($medizco_team_offset != '') {
            $query['offset'] = $medizco_team_offset;
        }

        $doctors_query = new \WP_Query( $query );

        // Slider Attributes
        $this->add_render_attribute( 'slider_wrap', 'data-rtl', is_rtl() );
        ?>

        <div class="medizco_doctors <?php echo esc_html( $medizco_doctors_style ); ?>" <?php echo $this->get_render_attribute_string( 'slider_wrap' ); ?>>
            <?php
            if ( $doctors_query->have_posts() ):
                if ( 'medizco_doctors_filter' == $medizco_doctors_style ):
                    get_template_part( '/template-parts/doctors/doctors-filter-nav' );

                    echo '<div class="filter_items row">';
                endif;

                while ( $doctors_query->have_posts() ):
                    $doctors_query->the_post();

                    // Slider
                    if ( 'medizco_doctors_slider' == $medizco_doctors_style ):
                        get_template_part( '/template-parts/doctors/doctor-box' );
                    endif;

                    // Filter
                    if ( 'medizco_doctors_filter' == $medizco_doctors_style ):
                        $cur_departs = get_the_terms( get_the_ID(), 'medizco-departments' );
                        $cur_deprts_classlist = '';

                        foreach ( $cur_departs as $cur_depart ):
                            $cur_deprts_classlist .= ' ' . $cur_depart->slug;
                        endforeach;

                        echo '<div class="filter_item mix col-lg-3 col-md-6 col-sm-12'. $cur_deprts_classlist .'">';
                            get_template_part( '/template-parts/doctors/doctor-box' );
                        echo '</div>';
                    endif;
                endwhile;
                wp_reset_postdata();

                if ( 'medizco_doctors_filter' == $medizco_doctors_style ):
                    echo '</div>';
                endif;
            endif;
            ?>
        </div>
        <?php
    }

    protected function content_template() { }

    public function getCategories( $term ){
        $terms = get_terms(array(
            'taxonomy'          => $term,
            'hide_empty'        => false,
            'posts_per_page'    => -1,
        ));

        $cat_list = [];
        if ( is_array($terms) && '' != $terms ) :
            foreach($terms as $post) {

                $cat_list[$post->term_id]  = [$post->name];
            }
        endif;
        return $cat_list;
    }
}