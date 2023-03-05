<template>
  <Slider
    class="app-slider"
    :value="value"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <template
      v-for="(_, slot) of $scopedSlots"
      v-slot:[slot]="scope"
    >
      <slot
        :name="slot"
        v-bind="scope"
      />
    </template>
  </Slider>
</template>

<script>
export default {
  name: 'AppSlider',
  props: {
    value: {
      type: Number,
      default: 1,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.app-slider {
  &.p-slider {
    background: $gray-dd;
    border: 0 none;
    border-radius: 3px;
  }
  &.p-slider.p-slider-horizontal {
    height: 0.286rem;
  }
  &.p-slider.p-slider-horizontal .p-slider-handle {
    top: -1.2rem;
    margin-left: -1.3715rem;
  }
  &.p-slider .p-slider-handle {
    height: 3rem;
    width: 3rem;
    background: $primary;
    border-radius: 50%;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  }
  &.p-slider .p-slider-handle:focus {
    outline: 0 none;
    outline-offset: 0;
    box-shadow: 0 0 0 0.2rem #a6d5fa;
  }
  &.p-slider .p-slider-range {
    background: $primary;
  }
  &.p-slider:not(.p-disabled) .p-slider-handle:hover {
    background: #2196F3;
    border-color: #2196F3;
  }
}
</style>
