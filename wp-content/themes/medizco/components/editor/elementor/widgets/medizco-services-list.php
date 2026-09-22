<?php

namespace Elementor;

if ( ! defined( 'ABSPATH' ) ) exit;

class Medizco_Services_List_Widget extends Widget_Base {

    public function get_name() {
        return 'medizco-services-list';
    }


    public function get_title() {
        return esc_html__( 'Medizco Services List', 'medizco' );
    }

    public function get_icon() {
        return 'eicon-bullet-list';
    }

    public function get_categories() {
        return ['medizco-elements'];
    }

    protected function register_controls() {

        $this->start_controls_section(
            'medizco_serviceslist_contents',
            [
                'label'         => __( 'Contents', 'medizco' ),
                'tab'           => Controls_Manager::TAB_CONTENT,
                'label_block'   => true,
            ]
        );
            $this->add_control(
                'medizco_serviceslist_count',
                [
                    'label'         => __( 'Max List Count', 'medizco' ),
                    'type'          => Controls_Manager::NUMBER,
                    'default'       => __( '12', 'medizco' ),
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section(
            'medizco_serviceslist_styles',
            [
                'label'         => __( 'List', 'medizco' ),
                'tab'           => Controls_Manager::TAB_STYLE,
                'label_block'   => true,
            ]
        );
            $this->start_controls_tabs( 'medizco_serviceslist_link_tabs' );
                $this->start_controls_tab(
                    'medizco_serviceslist_link_tab_1',
                    [
                        'label' => __( 'Normal', 'medizco' ),
                    ]
                );
                    $this->add_control(
                        'medizco_serviceslist_link_color_n',
                        [
                            'label'     => __( 'Color', 'medizco' ),
                            'type'      => Controls_Manager::COLOR,
                            'default'   => '',
                            'selectors' => [
                                '{{WRAPPER}} a' => 'color: {{VALUE}}'
                            ],
                        ]
                    );

                    $this->add_control(
                        'medizco_serviceslist_link_bgcolor_n',
                        [
                            'label'     => __( 'Background Color', 'medizco' ),
                            'type'      => Controls_Manager::COLOR,
                            'default'   => '',
                            'selectors' => [
                                '{{WRAPPER}} a' => 'background-color: {{VALUE}}'
                            ],
                        ]
                    );
                $this->end_controls_tab();

                $this->start_controls_tab(
                    'medizco_serviceslist_link_tab_2',
                    [
                        'label' => __( 'Hover', 'medizco' ),
                    ]
                );
                    $this->add_control(
                        'medizco_serviceslist_link_color_h',
                        [
                            'label'     => __( 'Color', 'medizco' ),
                            'type'      => Controls_Manager::COLOR,
                            'default'   => '',
                            'selectors' => [
                                '{{WRAPPER}} a:hover' => 'color: {{VALUE}}'
                            ],
                        ]
                    );

                    $this->add_control(
                        'medizco_serviceslist_link_bgcolor_h',
                        [
                            'label'     => __( 'Background Color', 'medizco' ),
                            'type'      => Controls_Manager::COLOR,
                            'default'   => '',
                            'selectors' => [
                                '{{WRAPPER}} a:hover' => 'background-color: {{VALUE}}'
                            ],
                        ]
                    );
                $this->end_controls_tab();
            $this->end_controls_tabs();

            $this->add_responsive_control(
                'medizco_serviceslist_link_pd',
                [
                    'label'         => __( 'Padding', 'medizco' ),
                    'type'          => Controls_Manager::DIMENSIONS,

                    'size_units'    => [ 'px', '%', 'em' ],
                    'selectors'     => [
                        '{{WRAPPER}} a' => 'padding: {{TOP}}{{UNIT}} {{RIGHT}}{{UNIT}} {{BOTTOM}}{{UNIT}} {{LEFT}}{{UNIT}};',
                    ],
                    'separator'     => 'before',
                ]
            );
        $this->end_controls_section();
    }

    protected function render( ) {
        $settings = $this->get_settings_for_display();

        $cur_page_id = get_the_ID();
        
        $paged = 1;
        if ( get_query_var('paged') ) $paged = get_query_var('paged');
        if ( get_query_var('page') ) $paged = get_query_var('page');

        $query = array(
            'post_type'     => 'medizco-service',
            'post_status'   => 'publish',
            'posts_per_page'=> $settings['medizco_serviceslist_count'],
            'paged'         => $paged
        );

        $services_query = new \WP_Query( $query );

        if ( $services_query->have_posts() ):
        ?>
            <ul class="medizco_servics_list">
                <?php
                while ( $services_query->have_posts() ):
                    $services_query->the_post();

                    $service_title = medizco_meta_option( get_the_ID(), 'header_title' );

                    $active_class = $cur_page_id == get_the_ID() ? 'active' : '';
                    ?>
                        <li>
                            <a href="<?php the_permalink(); ?>" class="<?php echo esc_attr( $active_class ); ?>">
                                <span><?php echo esc_html( $service_title ) ? esc_html( $service_title ) : get_the_title(); ?></span>
                                <i class="fa fa-chevron-right"></i>
                            </a>
                        </li>
                    <?php
                endwhile;
                wp_reset_postdata();
                ?>
            </ul>
        <?php
        endif;
    }

    protected function content_template() { }
}