import { TestBed } from '@angular/core/testing';

import { SamplingService } from './sampling.service';

describe('MicrosampleService', () => {
  let service: SamplingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SamplingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
