import { Component, OnInit, Input } from '@angular/core';
import { VideoInfo } from '../video-info-module';
import { YoutubeSearchService } from 'src/app/services/youtube-search.service';
import {  NgxSpinnerService } from 'ngx-spinner'

@Component({
  selector: 'app-search-result',
  templateUrl: './search-result.component.html',
  styleUrls: ['./search-result.component.css']
})
export class SearchResultComponent implements OnInit {
  @Input() result: VideoInfo;
  comments: any;

  constructor(private youtubesearchservice: YoutubeSearchService, private spinner: NgxSpinnerService ) {}


  ngOnInit(): void {
    this.spinner.show()
    setTimeout(()=>{this.spinner.hide()},3000)
  }

  onClick(){
    this.youtubesearchservice.saveVideoComments(this.result.id).subscribe(
      (data) => {
        this.comments = data;
        var response = JSON.stringify(data);
        console.log(data);
      }
    )
  }


}
