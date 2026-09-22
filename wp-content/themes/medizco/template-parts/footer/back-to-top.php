<?php

$back_to_top = medizco_option( 'back_to_top' );

if ( 'show' == $back_to_top ):
?>
   <div class="BackTo">
      <a href="#" class="fa fa-angle-up" aria-hidden="true"></a>
   </div>
<?php
endif;
