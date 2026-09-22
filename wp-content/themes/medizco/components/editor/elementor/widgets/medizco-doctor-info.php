<?php

namespace Elementor;

if ( ! defined( 'ABSPATH' ) ) exit;

class Medizco_Doctor_Info_Widget extends Widget_Base {

    public function get_name() {
        return 'medizco-doctor-info';
    }


    public function get_title() {
        return esc_html__( 'Medizco Doctor Info', 'medizco' );
    }

    public function get_icon() {
        return 'eicon-toggle';
    }

    public function get_categories() {
        return ['medizco-elements'];
    }

    protected function register_controls() {
        $this->start_controls_section(
            'docinfo_block',
            [
                'label'         => __( 'Contents', 'medizco' ),
                'tab'           => Controls_Manager::TAB_CONTENT,
            ]
        );
            $repeater = new \Elementor\Repeater();

            $repeater->add_control(
                'docinfo_th', [
                    'label'         => __( 'Title:', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::TEXT,
                    'label_block'   => true,
                ]
            );

            $repeater->add_control(
                'docinfo_td_type',
                [
                    'label'         => __( 'Text', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::SELECT,
                    'label_block'   => true,
                    'default'       => 'custom',
                    'options'       => [
                        'none'          => __( 'None', 'medizco' ),
                        'title'         => __( 'Page Title', 'medizco' ),
                        'role'          => __( 'Primary Specialty', 'medizco' ),
                        'custom'        => __( 'Custom Text', 'medizco' ),
                    ],
                ]
            );

            $repeater->add_control(
                'docinfo_td', [
                    'label'         => __( 'Custom Text:', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::TEXT,
                    'label_block'   => true,
                    'condition' => [
                        'docinfo_td_type' => 'custom',
                    ],
                ]
            );
            
            $repeater->add_control(
                'docinfo_td_st',
                [
                    'label'         => __( 'Space Top', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::NUMBER,
                    'condition' => [
                        'docinfo_td_type' => 'none',
                    ],
                ]
            );
            
            $repeater->add_control(
                'docinfo_td_sb',
                [
                    'label'         => __( 'Space Bottom', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::NUMBER,
                    'condition' => [
                        'docinfo_td_type' => 'none',
                    ],
                ]
            );

            $this->add_control(
                'docinfo_list',
                [
                    'label'         => __( 'Info List', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::REPEATER,
                    'fields'        => $repeater->get_controls(),
                    'default'       => [
                        [
                            'docinfo_th'        => __( 'Doctor Name', 'medizco' ),
                            'docinfo_td_type'   => 'title',
                        ],
                        [
                            'docinfo_th'        => __( 'Primary Specialty', 'medizco' ),
                            'docinfo_td_type'   => 'role',
                        ],
                    ],
                    'title_field'   => '{{{ docinfo_th }}}',
                ]
            );

        $this->end_controls_section();

        $this->start_controls_section(
            'docinfo_style',
            [
                'label'         => __( 'Style', 'medizco' ),
                'tab'           => Controls_Manager::TAB_STYLE,
            ]
        );
            $this->add_control(
                'docinfo_color',
                [
                    'label'     => __( 'Color', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '#222',
                    'selectors' => [
                        '{{WRAPPER}} .medizco-doctor-info' => 'color: {{VALUE}}',
                    ],
                ]
            );

            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'docinfo_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .medizco-doctor-info',
                    'fields_options'    => [
                        'font_size' => [
                            'default'   => [
                                'unit'  => 'px',
                                'size'  => 16
                            ]
                        ],
                        'font_weight' => [
                            'default'   => 500
                        ],
                    ],
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section(
            'docinfo_headings_style',
            [
                'label'         => __( 'Heading', 'medizco' ),
                'tab'           => Controls_Manager::TAB_STYLE,
            ]
        );
            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'docinfo_headings_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .medizco-doctor-info .heading',
                ]
            );
        $this->end_controls_section();
    }

    protected function render( ) {
        $settings = $this->get_settings_for_display();
        ?>
        <div class="medizco-doctor-info">
            <table>
                <tbody>
                    <?php
                    if ( $settings['docinfo_list'] ):
                        foreach ( $settings['docinfo_list'] as $docinfoItem ):
                            $docinfoItemTh = $docinfoItem['docinfo_th'];

                            switch ( $docinfoItem['docinfo_td_type'] ) {
                                case 'title':
                                    $headerTitle = medizco_meta_option( get_the_ID(), 'header_title' );
                                    $headerTitle = empty( $headerTitle ) ? get_the_title() : $headerTitle;

                                    $docinfoItemTd = $headerTitle;
                                break;

                                case 'role':
                                    $docrole = medizco_meta_option( get_the_ID(), 'doctor_role' );
                                    $docinfoItemTd = $docrole;
                                break;

                                case 'custom':
                                    $docinfoItemTd = $docinfoItem['docinfo_td'];
                                break;

                                default:
                                    $docinfoItemTd = '';
                            }
                        ?>
                        <tr>
                            <?php
                                if ( 'none' === $docinfoItem['docinfo_td_type'] ):
                                    $space_top = $docinfoItem['docinfo_td_st'] !== '' ? 'padding-top: '. $docinfoItem['docinfo_td_st'] .'px;' : '';
                                    $space_bottom = $docinfoItem['docinfo_td_sb'] !== '' ? ' padding-bottom: '. $docinfoItem['docinfo_td_sb'] .'px;' : '';
                                    ?>
                                    <th colspan="2" class="heading" style="<?php echo esc_attr( $space_top.$space_bottom ); ?>"><?php echo esc_html( $docinfoItemTh ); ?></th>
                            <?php else: ?>
                                <th><?php echo esc_html( $docinfoItemTh ); ?></th>
                                <td><?php echo esc_html( $docinfoItemTd ); ?></td>
                            <?php endif; ?>
                        </tr>
                        <?php
                        endforeach;
                    endif;
                    ?>
                </tbody>
            </table>
        </div>
        <?php
    }

    protected function content_template() {}
}
