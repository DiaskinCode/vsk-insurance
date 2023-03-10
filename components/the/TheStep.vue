<template>
  <div class="step container py-100 fd-c ai-c pt-50-mb pb-0-mb">
    <h2 class="header-text ta-c">
      Полис оформить просто<br class="d-n-mb">
      в течение 2-х минут в 4 шага:
    </h2>
    <div class="mt-60 mw-100 ove-h">
      <AppTimeline
        class="pl-130 pr-0 fs-20 lh-140 pl-0-mb fs-16-mb"
        :layout="layout"
        :value="steps"
      >
        <template v-slot:marker="{ index }">
          <div
            class="step__marker bg-gf5 br-c d-f ai-c jc-c fw-6 fs-25"
          >
            {{ index }}
          </div>
        </template>
        <template v-slot:content="{ item }">
          <div class="step__content ta-c px-20 ta-l-mb pl-20-mb">
            <div
              v-for="(text, i) in item"
              :key="i"
              class="ws-nw"
            >
              {{ text }}
            </div>
          </div>
        </template>
      </AppTimeline>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheStep',
  props: {},
  data: () => ({
    steps: [
      [
        'Заполнить данные',
        'по Застрахованному',
        'и Страхователю',
      ],
      [
        'Выбрать вид спорта',
        'из доступного перечня',
        '(более 20 наименований)',
      ],
      [
        'Выбрать срок',
        'страхования',
      ],
      [
        'Оплатить полис',
      ],
    ],
  }),
  computed: {
    layout() {
      return this.$mq === 'mb' ? 'vertical' : 'horizontal';
    },
  },
  methods: {},
}
</script>

<style lang="scss">
.step {
  /* .step__marker */
  &__marker {
    width: 4.4rem;
    min-width: 4.4rem;
    height: 4.4rem;
    min-height: 4.4rem;
  }
  /* .step__content */
  &__content {
    transform: translateX(-42%);
    @media (max-width: 600px) {
      transform: none;
    }
  }

  .p-timeline-event {
    min-width: 30.8rem;
    width: 30.8rem;
  }
  .p-timeline-event:last-child {
    .step__content {
      transform: translateX(-40%);
      @media (max-width: 600px) {
        transform: none;
      }
    }
  }
  .p-timeline-event-separator {
    min-width: 30.8rem;
    width: 30.8rem;
    @media (max-width: 600px) {
      min-width: unset;
    }
    @media (max-width: 600px) {
      min-height: 10rem;
    }
  }
}
</style>
