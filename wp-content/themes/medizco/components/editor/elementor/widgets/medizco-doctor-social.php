<?php

namespace Elementor;

if ( ! defined( 'ABSPATH' ) ) exit;

class Medizco_Doctor_Social_Widget extends Widget_Base {

    public function get_name() {
        return 'medizco-doctor-social';
    }


    public function get_title() {
        return esc_html__( 'Medizco Doctor Social', 'medizco' );
    }

    public function get_icon() {
        return 'eicon-social-icons';
    }

    public function get_categories() {
        return ['medizco-elements'];
    }

    protected function register_controls() {

        $this->start_controls_section(
            'docsocial_block1',
            [
                'label'         => __( 'Contents', 'medizco' ),
                'tab'           => Controls_Manager::TAB_CONTENT,
                'label_block'   => true,
            ]
        );

            $this->add_control(
                'docsocial_title',
                [
                    'label'         => __( 'Title', 'medizco' ),
                    'type'          => Controls_Manager::TEXT,
                    'label_block'   => true,
                    'default'       => __( 'Social Media', 'medizco' ),
                ]
            );

        $this->end_controls_section();

        $this->start_controls_section(
            'docsocial_block2',
            [
                'label'         => __( 'Title', 'medizco' ),
                'tab'           => Controls_Manager::TAB_STYLE,
                'label_block'   => true,
            ]
        );
        
            $this->add_control(
                'docsocial_title_color',
                [
                    'label'     => __( 'Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#222',
                    'selectors' => [
                        '{{WRAPPER}} .medizco-doctor-social-widget > h3' => 'color: {{VALUE}}',
                    ],
                ]
            );

            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'docsocial_title_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .medizco-doctor-social-widget > h3',
                    'fields_options'    => [
                        'font_size' => [
                            'default'   => [
                                'unit'  => 'px',
                                'size'  => 28
                            ]
                        ],
                    ],
                ]
            );

            $this->add_control(
                'docsocial_title_margin',
                [
                    'label'         => __( 'Margin', 'medizco' ),
                    'type'          => Controls_Manager::DIMENSIONS,
                    'size_units'    => [ 'px' ],
                    'selectors'     => [
                        '{{WRAPPER}} .medizco-doctor-social-widget > h3' => 'margin: {{TOP}}{{UNIT}} {{RIGHT}}{{UNIT}} {{BOTTOM}}{{UNIT}} {{LEFT}}{{UNIT}};',
                    ],
                ]
            );

        $this->end_controls_section();

    }

    protected function render( ) {
        $settings = $this->get_settings_for_display();

        $doctor_sc_icons = medizco_meta_option( get_the_ID(), 'doctor_social' );
        ?>

        <div class="medizco-doctor-social-widget">
            <?php if ( $settings['docsocial_title'] ): ?>
            <h3><?php echo esc_html( $settings['docsocial_title'] ); ?></h3>
            <?php endif; ?>

            <?php if ( !empty( $doctor_sc_icons ) ): ?>
            <ul>
                <?php foreach ( $doctor_sc_icons as $doctor_sc_icon ): ?>
                <li>
                    <a href="<?php echo esc_url( $doctor_sc_icon['link'] ); ?>" target="_blank" style="background-color: <?php echo esc_attr( $doctor_sc_icon['color'] ); ?>;">
                        <i class="<?php echo esc_attr( $doctor_sc_icon['icon'] ); ?>"></i>
                    </a>
                </li>
                <?php endforeach; ?>
            </ul>
            <?php endif; ?>
        </div>

        <?php
    }

    protected function content_template() { }
}
